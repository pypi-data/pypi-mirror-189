from pytest import raises

from stateful import StatefulObject, stateful_property


def test_readonly_property():
    class TestClass(StatefulObject):
        def __init__(self):
            self._ro = 0

        @stateful_property
        def ro_property(self):
            return self._ro

        @ro_property.refresher
        def ro_property(self):
            self._ro += 1

    test_data = TestClass()
    assert test_data.get_stateful_properties() == {"ro_property": TestClass.ro_property}

    assert test_data.ro_property == 0
    with raises(AttributeError):
        test_data.ro_property = 1
    test_data.refresh()
    assert test_data.ro_property == 1
    test_data.refresh("nonexistent")
    assert test_data.ro_property == 1
    test_data.refresh(("ro_property", "nonexistent"))
    assert test_data.ro_property == 2
    test_data.commit()
    assert test_data.ro_property == 2


def test_readwrite_property():
    class TestClass(StatefulObject):
        def __init__(self):
            self._rw = 0

        @stateful_property
        def rw_property(self):
            return self._rw

        @rw_property.setter
        def rw_property(self, value):
            self._rw_cache = value

        @rw_property.refresher
        def rw_property(self):
            self._rw = 0
            if hasattr(self, "_rw_cache"):
                del self._rw_cache

        @rw_property.committer
        def rw_property(self):
            self._rw = self._rw_cache
            if hasattr(self, "_rw_cache"):
                del self._rw_cache

    test_data = TestClass()
    assert test_data.get_stateful_properties() == {"rw_property": TestClass.rw_property}

    assert test_data.rw_property == 0
    with raises(AttributeError):
        test_data.commit()
    test_data.rw_property = 1
    assert test_data.rw_property == 0
    test_data.commit("rw_property")
    assert test_data.rw_property == 1
    setattr(test_data, "rw_property", 12)
    test_data.commit()
    assert test_data.rw_property == 12
    test_data.refresh()
    assert test_data.rw_property == 0


def test_autocommit():
    def TestClass(StatefulObject):
        def __init__(self):
            super().__init__(True)
