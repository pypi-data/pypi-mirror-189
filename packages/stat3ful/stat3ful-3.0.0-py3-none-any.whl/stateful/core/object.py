from typing import Iterable, Optional, Set, Union

from .property import stateful_property
from .state import ObjectState


class StatefulObject:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__state__ = ObjectState()
        for key in dir(cls):
            value = getattr(cls, key)
            if isinstance(value, stateful_property):
                instance.__state__.register(value, (key,))
        return instance

    def __init__(self, auto_commit: bool = False):
        self.auto_commit = auto_commit

    @property
    def expired(self) -> Set[str]:
        return {
            property.alias for property, state in self.state.items() if state.expired
        }

    @property
    def state(self) -> ObjectState:
        return self.__state__

    def get_properties(
        self,
        property_spec: Optional[
            Union[
                str,
                Iterable[str],
            ]
        ] = None,
    ) -> Set[stateful_property]:
        if property_spec in ("*", None):
            return set(self.state.keys())
        if isinstance(property_spec, str):
            property_spec = (property_spec,)
        if isinstance(property_spec, Iterable):
            output = set()
            for property_alias in property_spec:
                property = self.state.__aliases__.get(property_alias)
                if property:
                    output.add(property)
            return output
        raise TypeError("invalid property specifier, string(s) required")

    def refresh(
        self,
        property_spec: Optional[
            Union[
                str,
                Iterable[str],
            ]
        ] = None,
        *,
        force: bool = True,
    ):
        for property in self.get_properties(property_spec):
            property_state = self.state[property]
            if property_state.expired or force:
                property.refresh(self)

    def commit(
        self,
        property_spec: Optional[
            Union[
                str,
                Iterable[str],
            ]
        ] = None,
        *,
        force: bool = True,
    ):
        for property in self.get_properties(property_spec):
            property_state = self.state[property]
            if property_state.changed or force:
                property.commit(self)
