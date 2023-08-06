from typing import Any, Callable, Optional, Type

from .state import PropertyState

FALLBACK_METHOD = object()


class StatefulPropertyWrapper:
    def __init__(self, state: PropertyState, value: Any):
        self.expired = getattr(state, "expired", None)
        self.changed = getattr(state, "changed", None)
        self.__value__ = value

    @property
    def __class__(self) -> Type:
        return self.__value__.__class__

    def __getattr__(self, attrname: str) -> Any:
        if attrname not in ("expired", "changed", "__value__"):
            return getattr(self.__value__, attrname)

    def __setattr__(self, attrname: str, value: Any):
        if attrname in ("expired", "changed", "__value__"):
            object.__setattr__(self, attrname, value)
        else:
            self.__value__ = value

    def __eq__(self, other: Any) -> bool:
        return self.__value__ == other

    def __gt__(self, other: Any) -> bool:
        return self.__value__ > other

    def __str__(self) -> str:
        return self.__value__.__str__()

    def __repr__(self) -> str:
        return self.__value__.__repr__()


class stateful_property:
    def __init__(
        self,
        fget: Optional[
            Callable[
                [
                    Any,
                ],
                Any,
            ]
        ] = None,
        fset: Optional[
            Callable[
                [
                    Any,
                    Any,
                ],
                None,
            ]
        ] = None,
        fdel: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = None,
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
        raw: bool = False,
    ):
        self.alias = f"{self.__class__.__name__}[{id(self)}]"
        self.getter(fget)
        self.setter(fset)
        self.deleter(fdel)
        self.refresher(frefresh)
        self.committer(fcommit)
        self.auto_commit = auto_commit
        self.raw = raw

    def getter(
        self,
        fget: Optional[
            Callable[
                [
                    Any,
                ],
                Any,
            ]
        ] = None,
    ):
        self.fget = (
            getattr(self, "fallback_getter", None) if fget is FALLBACK_METHOD else fget
        )
        return self

    def setter(
        self,
        fset: Optional[
            Callable[
                [
                    Any,
                    Any,
                ],
                None,
            ]
        ] = None,
    ):
        self.fset = (
            getattr(self, "fallback_setter", None) if fset is FALLBACK_METHOD else fset
        )
        return self

    def deleter(
        self,
        fdel: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = None,
    ):
        self.fdel = (
            getattr(self, "fallback_deleter", None) if fdel is FALLBACK_METHOD else fdel
        )
        return self

    def fallback_refresher(
        self,
        stateful_object: Any,
    ):
        pass

    def fallback_committer(
        self,
        stateful_object: Any,
    ):
        pass

    def refresh(self, owner: Any) -> Any:
        if self.frefresh is None:
            raise AttributeError(f"can't refresh attribute {self.alias}")
        output = self.frefresh(owner)
        state = getattr(owner, "state", {}).get(self)
        if state:
            state.expired = False
            state.changed = False
        return output

    def commit(self, owner: Any):
        if self.fcommit is None:
            raise AttributeError(f"non-commitable attribute {self.alias}")
        output = (self.fcommit if self.fcommit else self.fallback_commit)(owner)
        state = getattr(owner, "state", {}).get(self)
        if state:
            state.expired = False
            state.changed = False
        return output

    def refresher(
        self,
        frefresh: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
    ):
        self.frefresh = (
            getattr(self, "fallback_refresher", None)
            if frefresh is FALLBACK_METHOD
            else frefresh
        )
        return self

    def committer(
        self,
        fcommit: Optional[
            Callable[
                [
                    Any,
                ],
                None,
            ]
        ] = FALLBACK_METHOD,
    ):
        self.fcommit = (
            getattr(self, "fallback_committer", None)
            if fcommit is FALLBACK_METHOD
            else fcommit
        )
        return self

    def __touch__(self, owner: Any):
        state = getattr(owner, "state", {}).get(self)
        if state:
            state.changed = True
            if (
                getattr(owner, "auto_commit", False)
                if self.auto_commit is None
                else self.auto_commit
            ):
                self.commit(owner)

    def __get__(self, owner: Any, cls: Optional[type] = None):
        if owner is None:
            return self
        if self.fget is None:
            raise AttributeError(f"unreadable attribute {self.alias}")
        state = getattr(owner, "state", {}).get(self)
        if state and state.expired:
            self.refresh(owner)
        output = self.fget(owner)
        return output if self.raw else StatefulPropertyWrapper(state, output)

    def __set__(self, owner: Any, value: Any):
        if self.fset is None:
            raise AttributeError(f"can't set attribute {self.alias}")
        self.fset(owner, value)
        self.__touch__(owner)

    def __delete__(self, owner: Any):
        if self.fdel is None:
            raise AttributeError(f"can't delete attribute {self.alias}")
        self.fdel(owner)
        self.__touch__(owner)

    def __set_name__(self, owner: Any, name: str):
        self.alias = name

    def __call__(
        self,
        fget: Callable[
            [
                Any,
                Optional[type],
            ],
            Any,
        ],
    ) -> property:
        self.getter(fget)
        return self
