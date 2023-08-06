import typing
from itertools import count


class PropertyOwner:
    def __init__(self, expired=False, auto_commit=False):
        self.expired = expired
        self.auto_commit = auto_commit


def function_factory(data, index):
    def test_function(*args):
        data[index] += len(args)

    return test_function


def generate_test_functions():
    data = [0, 0, 0, 0, 0]
    return data, [function_factory(data, index) for index in range(5)]


def generate_stateful_object():
    from stateful import StatefulObject

    class TestClass(StatefulObject):
        @classmethod
        def get_stateful_properties(cls, property_spec):
            if property_spec in ("*", None):
                property_spec = ["expired", "auto_commit"]
            elif isinstance(property_spec, str):
                property_spec = [property_spec]
            if isinstance(property_spec, typing.Iterable):
                output = {}
                for property_name in property_spec:
                    property = getattr(cls, property_name, None)
                    output[property_name] = property
                return output
            raise TypeError()

        def __init__(self):
            super().__init__(True)

        @property
        def expired(self):
            self._expired = not getattr(self, "_expired", False)
            return self._expired

        @expired.setter
        def expired(self, value):
            self._expired = value

        def refresh(self, property_spec=None):
            for property_name, _ in self.get_stateful_properties(property_spec).items():
                setattr(self, property_name, False)

        def commit(self, property_spec=None):
            for property_name, _ in self.get_stateful_properties(property_spec).items():
                setattr(self, property_name, True)

    return TestClass()


class TimerEmulator:
    def __init__(self):
        self.access_counter = 0
        self.timer = count()

    def refresh(self, property_spec=None):
        self.access_counter += 1
