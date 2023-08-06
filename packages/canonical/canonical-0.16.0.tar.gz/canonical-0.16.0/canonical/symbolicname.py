# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import re
from typing import Any
from typing import Callable
from typing import Generator

from pydantic.validators import str_validator


class SymbolicName(str):

    @classmethod
    def __modify_schema__(
        cls,
        field_schema: dict[str, Any]
    ) -> None:
        field_schema.update( # pragma: no cover
            title='Symbolic Name',
            type='string',
        )

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., str | None], None, None]:
        yield str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Symbolic name is too short.")
        if len(v) > 31:
            raise ValueError("Symbolic name is too long.")
        if not re.match('^[a-z][a-z0-9\\-]+[a-z0-9]$', v):
            raise ValueError("Invalid characters.")
        return v

    def __repr__(self) -> str: # pragma: no cover
        return f'SymbolicName({self})'