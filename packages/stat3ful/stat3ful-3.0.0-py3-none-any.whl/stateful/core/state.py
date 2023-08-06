from contextlib import nullcontext
from threading import RLock
from typing import Iterable, Optional, Union, Tuple


class PropertyState:
    def __init__(self, target: property, lock: Optional[RLock] = None):
        self._lock = lock if lock else RLock()
        self.target = target
        self.expired = False
        self.changed = False

    @property
    def expired(self) -> bool:
        with self._lock:
            return getattr(self, "_expired", False)

    @expired.setter
    def expired(self, value: bool):
        with self._lock:
            self._expired = bool(value)

    @property
    def changed(self) -> bool:
        with self._lock:
            return getattr(self, "_changed", False)

    @changed.setter
    def changed(self, value: bool):
        with self._lock:
            self._changed = bool(value)

    @property
    def lock(self) -> RLock:
        with self._lock:
            return self._lock

    @lock.setter
    def lock(self, value: Optional[RLock]):
        with self._lock:
            self._lock = value if value else RLock()


class ObjectState:
    def __init__(self, atomic: bool = True):
        self.__statetable__ = {}
        self.__aliases__ = {}
        self.atomic = atomic

    @property
    def atomic(self):
        return not getattr(self, "_synchroniser", None) is None

    @atomic.setter
    def atomic(self, value: bool):
        value = bool(value)
        if self.atomic != value:
            self._lock = RLock() if value else nullcontext()
            self._synchroniser = self._lock if value else None
            with self._lock:
                for property_state in self.__statetable__.values():
                    property_state.lock = self._synchroniser

    def invalidate(self):
        with self._lock:
            for property_state in self.__statetable__.values():
                property_state.expired = True

    def register(self, obj_property: property, aliases: Iterable[str] = []):
        with self._lock:
            self.__statetable__[obj_property] = getattr(
                obj_property, "state_class", PropertyState
            )(obj_property, getattr(self, "_synchroniser", None))
            for alias in aliases:
                self.__aliases__[alias] = obj_property

    def unregister(self, obj_property: property):
        del self.__statetable__[obj_property]
        for alias in [
            alias
            for alias, target in self.__aliases__.items()
            if target is obj_property
        ]:
            del self.__aliases__[alias]

    def __getitem__(self, key: Union[str, property]) -> PropertyState:
        if isinstance(key, str):
            key = self.__aliases__[key]
        return self.__statetable__[key]

    def get(self, key: Union[str, property]) -> Optional[PropertyState]:
        if isinstance(key, str):
            key = self.__aliases__[key]
        return self.__statetable__.get(key)

    def keys(self)->Iterable[property]:
        return self.__statetable__.keys()

    def values(self)->Iterable[PropertyState]:
        return self.__statetable__.values()

    def items(self)->Iterable[Tuple[property, PropertyState]]:
        return self.__statetable__.items()

    def aliases(self)->Iterable[Tuple[str, property]]:
        return self.__aliases__.items()
