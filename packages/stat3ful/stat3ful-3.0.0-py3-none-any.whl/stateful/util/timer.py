from datetime import datetime, timedelta
from threading import RLock
from typing import Any, Callable, Dict, Optional, Type, Union

from ..core.object import StatefulObject
from ..core.property import FALLBACK_METHOD, stateful_property
from ..core.state import PropertyState


class Timer:
    def __init__(self, **timespec: Dict[str, Union[int, float]]):
        self.period = timedelta(**timespec)

    def __iter__(self):
        return self

    def __next__(self):
        return datetime.now() + self.period


class TimedPropertyState(PropertyState):
    @property
    def timer(self) -> Optional[Timer]:
        with self._lock:
            return getattr(self, "__timer__", None)

    @timer.setter
    def timer(self, timespec: Optional[Dict[str, Union[int, float]]] = None):
        with self._lock:
            if timespec is None:
                self.__timer__ = None
            else:
                last_expired = self.expired
                null_timer = self.timer is None
                self.__timer__ = iter(self.__tclass__(**timespec))
                if null_timer ^ last_expired:
                    self._expires = next(self.__timer__)

    @property
    def expired(self) -> bool:
        with self._lock:
            if self.timer is None:
                return super().expired
            expires = getattr(self, "_expires", datetime.now())
            return datetime.now() >= expires

    @expired.setter
    def expired(self, value: bool):
        with self._lock:
            if self.timer is None:
                return super(TimedPropertyState, self.__class__).expired.fset(
                    self, value
                )
            elif not value:
                self._expires = next(self.timer)
            else:
                try:
                    delattr(self, "_expires")
                except AttributeError:
                    pass


class timed_property(stateful_property):
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
        timespec: Optional[Dict[str, float]] = None,
        timer_class: Type[Timer] = Timer,
        raw: bool = False,
        **kwargs,
    ):
        super().__init__(
            fget=fget,
            fset=fset,
            fdel=fdel,
            frefresh=frefresh,
            fcommit=fcommit,
            auto_commit=auto_commit,
            raw=raw,
            **kwargs,
        )

        base_state_class = getattr(super(), "state_class", PropertyState)
        try:
            if not issubclass(type(base_state_class), type) and callable(
                base_state_class
            ):
                base_state_class = getattr(base_state_class, "__annotations__", {}).get(
                    "return", PropertyState
                )
            if not issubclass(base_state_class, TimedPropertyState):
                base_state_class = type(
                    f"{self.alias}__timer",
                    (TimedPropertyState, base_state_class),
                    {"__tclass__": timer_class},
                )
        except (TypeError, ValueError):
            pass
        self._tstate_class = base_state_class
        self.timespec = timespec

    @property
    def timespec(self) -> Optional[Dict[str, Union[int, float]]]:
        return self._timespec

    @timespec.setter
    def timespec(self, value: Optional[Dict[str, Union[int, float]]]):
        self._timespec = value

        def state_class(
            target: Any, lock: Optional[RLock] = None
        ) -> self._tstate_class:
            instance = self._tstate_class(target, lock)
            instance.timer = self._timespec
            return instance

        self.state_class = state_class


class TimedStatefulObject(StatefulObject):
    def __init__(
        self,
        auto_commit: bool = False,
        timespec: Optional[Dict[str, Union[int, float]]] = None,
    ):
        super().__init__(auto_commit)
        self.timespec = timespec

    @property
    def timespec(self) -> Optional[Dict[str, Union[int, float]]]:
        return self._timespec

    @timespec.setter
    def timespec(self, value: Optional[Dict[str, Union[int, float]]]):
        self._timespec = value
        for property in self.get_properties():
            if isinstance(property, timed_property):
                property.timespec = value
                self.state[property].timer = value
