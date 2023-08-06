# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from types import EllipsisType
from typing import Any
from typing import Literal
from typing import TypeVar

import pydantic

from .objectmeta import BaseMeta
from .objectmeta import ObjectMeta


T = TypeVar('T')


class Config:
    named: bool = False
    namespaced = bool = False


class ResourceMetaclass(pydantic.main.ModelMetaclass):

    def __new__(
        cls,
        name: str,
        bases: tuple[type[Any]],
        namespace: dict[str, Any],
        **params: Any
    ) -> 'ResourceMetaclass':
        if not namespace.pop('__abstract__', False):
            ResourceConfig: type[Any] | None = namespace.get('Config')
            annotations = namespace.setdefault('__annotations__', {})

            # To support dynamic subclassing, inspect the bases to determine if this
            # class directly inherits from a Resource subclass. Use an instance
            # check instead of a subclass check to remove the need for circular
            # imports. Reconstruct the subclass parameters from the existing class.
            for b in bases:
                if isinstance(b, ResourceMetaclass) and hasattr(b, '_version'):
                    group, version = api_version = b._version # type: ignore

                    # These are needed to initialize the superclass if this is a
                    # third-generation subclass of Resource.
                    params['group'] = group
                    params['version'] = version

                    # Get the Config class from parent.
                    ResourceConfig = getattr(b, 'Config', None)

                    break
            else:
                group = params.get('group')
                version = api_version = params.get('version')
                ResourceConfig = namespace.get('Config')
            if group is not None:
                api_version = f'{group}/{version}'

            # Create or update the config.
            if ResourceConfig is None:
                ResourceConfig = namespace['Config'] = type('Config', (Config,), {})
            assert ResourceConfig is not None
            ResourceConfig.named = getattr(ResourceConfig, 'named', False)
            ResourceConfig.namespaced = getattr(ResourceConfig, 'namespaced', False)

            # Create the `spec` field if the user has not specified it.
            if annotations.get('spec'):
                ResourceSpec: type[pydantic.BaseModel] = annotations['spec']
                assert isinstance(ResourceSpec, pydantic.main.ModelMetaclass)
                namespace.setdefault(
                    'spec',
                    pydantic.Field(
                        default=...,
                        title=ResourceSpec.__name__,
                        description=(
                            f'The `spec` field defines the specification of the '
                            f'desired behavior or state of the **{name}**.'
                        )
                    )
                )

            # Ensure that the apiVersion, kind and metadata fields are present. Defaults
            # and constraints are set during subclass initialization.
            Metadata = annotations.setdefault('metadata', ObjectMeta)
            annotations['metadata'] = Metadata.clone(
                named=ResourceConfig.named
            )
            annotations.update({
                'api_version': Literal[api_version], # type: ignore
                'kind': Literal[name], # type: ignore
            })
            namespace.update({
                '__annotations__': annotations,
                '_version': (group, version),
                'api_version': pydantic.Field(
                    alias='apiVersion',
                    default=api_version,
                    description=(
                        'The `apiVersion` field defines the versioned schema of this'
                        'representation of an object. Servers should convert '
                        'recognized schemas to the latest internal value, and may '
                        'reject unrecognized values.'
                    )
                ),
                'kind': pydantic.Field(
                    default=name,
                    description=(
                        'The `kind` field is a string value representing the REST resource this '
                        'object represents. Servers may infer this from the endpoint '
                        'the client submits requests to. Cannot be updated.'
                        'In `CamelCase`.'
                    )
                ),
                'metadata': pydantic.Field(
                    default=...,
                    title='Metadata',
                    description="Standard object's metadata."
                )
            })

            # Determine if there is a status model.
            ResourceStatus: Any | None = namespace.pop('Status', None)
            if ResourceStatus is not None:
                annotations.update({
                    'status': ResourceStatus.model | None
                })
                namespace.update({
                    'status': pydantic.Field(
                        default=None,
                        title='Status',
                        description=f'Most recently observed status of the `{name}`.'
                    )
                })

        new_cls = super().__new__(cls, name, bases, namespace, **params) # type: ignore
        return new_cls # type: ignore

    def __getitem__(
        self: T,
        k: EllipsisType | tuple[EllipsisType, bool]
    ) -> T:
        namespace: dict[str, Any] = {}
        named: bool = False
        config: type[Config] = getattr(self, 'Config', Config)
        if isinstance(k, tuple):
            _, named, *_ = k
        return type(self.__name__, (self,), { # type: ignore
            **namespace,
            '__annotations__': {
                'metadata': BaseMeta.clone(
                    named=config.named or named
                )
            }
        })