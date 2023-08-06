# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
from typing import Any

import pydantic


class BaseMeta(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        default=None,
        title="Name",
        description=(
            "Name must be unique within a namespace. Is required when creating "
            "resources, although some resources may allow a client to request "
            "the generation of an appropriate name automatically. Name is "
            "primarily intended for creation idempotence and configuration "
            "definition. Cannot be updated.\n\n"
            "If the resource is not identified by symbolic names, but an "
            "auto-generated identifier instead, this field contains the "
            "same value as the `uid` field."
        )
    )

    namespace: str | None = pydantic.Field(
        default=None,
        title="Namespace",
        description=(
            "Namespace defines the space within which each name must be "
            "unique. An empty namespace is equivalent to the `default` "
            "namespace, but `default` is the canonical representation. "
            "Not all objects are required to be scoped to a namespace "
            "- the value of this field for those objects will be empty."
            "Not all servers may implement the concept of namespaces."
        )
    )

    labels: dict[str, str] = pydantic.Field(
        default={},
        title='Labels',
        description=(
            "Map of string keys and values that can be used to "
            "organize and categorize (scope and select) objects."
        )
    )

    annotations: dict[str, Any] = pydantic.Field(
        default={},
        title='Annotations',
        description=(
            "Annotations is an unstructured key value map stored "
            "with a resource that may be set by external tools "
            "to store and retrieve arbitrary metadata. They are "
            "not queryable and should be preserved when modifying"
            "objects."
        )
    )


class ObjectMeta(BaseMeta):
    generation: int = pydantic.Field(
        default=0,
        title='Generation',
        description=(
            "A sequence number representing a specific generation "
            "of the desired state. Populated by the system. Read-only."
        )
    )

    generate_name: bool | None = pydantic.Field(
        default=None,
        title="Generate name",
        alias='generateName',
        description=(
            "The `generateName` field is an optional prefix, used by the server, "
            "to generate a unique name ONLY IF the `name` field has not been "
            "provided. If this field is used, the `name` returned to the client "
            "will be different than the name passed. This value will also be "
            "combined with a unique suffix. The provided value has the same "
            "validation rules as the Name field, and may be truncated by the "
            "length of the suffix required to make the value unique on the server."
            "\n\n"
            "If this field is specified and the generated name exists, the "
            "server will return a 409."
        )
    )

    creation_timestamp: datetime.datetime | None = pydantic.Field(
        default=None,
        title="Created",
        alias='creationTimestamp',
        description=(
            "The `creationTimestamp` field is a timestamp representing "
            "the server time when this object was created. It is not "
            "guaranteed to be set in happens-before order across "
            "separate operations. Clients may not set this value and "
            "is ignored when provided."
            "It is represented in RFC3339 form and is in UTC."
        )
    )

    resource_version: str = pydantic.Field(
        default='pristine',
        title='Resource version',
        alias='resourceVersion',
        description=(
            "An opaque value that represents the internal version of "
            "this object that can be used by clients to determine when "
            "objects have changed. May be used for optimistic concurrency, "
            "change detection, and the watch operation on a resource or "
            "set of resources. Clients must treat these values as opaque "
            "and passed unmodified back to the server. They may only be "
            "valid for a particular resource or set of resources.\n\n"
            "Populated by the system. Read-only. Value must be treated "
            "as opaque by clients."
        )
    )

    uid: int | str | None = pydantic.Field(
        default=None,
        title="UID",
        description=(
            "UID is the unique in time and space value for this object. It "
            "is typically generated by the server on successful creation of "
            "a resource and is not allowed to change on PUT operations.\n\n"
            "Depending on the implementation, the `uid` field may be either "
            "an integer or a string, but clients should treat this value "
            "as opaque."
        )
    )

    links: dict[str, pydantic.AnyUrl] = pydantic.Field(
        default={},
        title='Links',
        description=(
            "A mapping of operations to links that may be used by clients "
            "to traverse the REStful API and discover additional "
            "methods on resources."
        )
    )

    class Config:
        allow_population_by_field_name: bool = True