from os import environ
from threading import RLock
from typing import Any, Callable, Optional

from ..core.property import FALLBACK_METHOD, stateful_property
from ..core.state import PropertyState


class EnvironmentVariableState(PropertyState):
    def __init__(self, target: property, lock: Optional[RLock] = None):
        super().__init__(target, lock)
        self.expired = True


class environment_variable(stateful_property):
    state_class = EnvironmentVariableState

    def __init__(
        self,
        varname: str,
        fget: Optional[
            Callable[
                [
                    Any,
                    Optional[type],
                ],
                Any,
            ]
        ] = FALLBACK_METHOD,
        fset: Optional[
            Callable[
                [
                    Any,
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
        fdel: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
        frefresh: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
        fcommit: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
        auto_commit: Optional[bool] = None,
        decoder: Callable[[str], Any] = lambda arg: arg,
        encoder: Callable[[Any], str] = str,
        **kwargs,
    ):
        super().__init__(
            fget=fget,
            fset=fset,
            fdel=fdel,
            frefresh=frefresh,
            fcommit=fcommit,
            auto_commit=auto_commit,
            **kwargs,
        )
        self.varname = varname
        self.decoder = decoder
        self.encoder = encoder

    @property
    def value(self) -> Any:
        value = environ.get(self.varname)
        return None if value is None else self.decoder(value)

    @value.setter
    def value(self, value: Any):
        if value is None:
            environ.pop(self.varname)
        else:
            environ.update(**{self.varname: self.encoder(value)})

    def fallback_getter(
        self,
        owner: Any,
    ) -> Any:
        return getattr(owner, f"_{self.alias}", None)

    def fallback_setter(
        self,
        owner: Any,
        value: Any,
    ):
        setattr(owner, f"_{self.alias}", value)

    def fallback_deleter(
        self,
        owner: Any,
    ):
        delattr(owner, f"_{self.alias}")

    def fallback_refresher(
        self,
        owner: Any,
    ):
        if self.fset is not None:
            self.fset(owner, self.value)

    def fallback_committer(
        self,
        owner: Any,
    ):
        if self.fget is not None:
            try:
                self.value = self.fget(owner)
            except AttributeError:
                self.value = None
