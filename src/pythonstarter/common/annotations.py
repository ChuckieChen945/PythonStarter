"""a location for custom annotations used in project."""

from __future__ import annotations

from collections.abc import Callable
from typing import Final, Literal, ParamSpec, Protocol, SupportsFloat, TypedDict, TypeVar

########################################################################################
# region Type Alias
########################################################################################


type JSONType = str | int | float | bool | None | dict[str, JSONType] | list[JSONType]
type Numeric = int | float | SupportsFloat

# endregion


########################################################################################
# region generics
########################################################################################

T = TypeVar("T")
P = ParamSpec("P")

# endregion


########################################################################################
# region protocols
########################################################################################


class Repository(Protocol[T]):
    """protocol example.

    Args:
        Protocol (_type_): _description_
    """

    def get(self, id_: int) -> T: ...


# endregion


########################################################################################
# region TypedDict
########################################################################################


class UserPayload(TypedDict):
    id: int
    name: str


# endregion


########################################################################################
# region callbacks
########################################################################################

OnSuccess = Callable[P, T]
OnError = Callable[P, T]


# endregion


########################################################################################
# region Literal / Final / Annotated
########################################################################################


Status = Literal["pending", "done", "failed"]
MAX_RETRY: Final = 3

# endregion
