from pytest import raises

from stateful.object import StatefulObject, StatefulObjectMeta

from .util import generate_stateful_object


class TestStatefulObjectMeta:
    def test_base(self):
        test_data = StatefulObjectMeta("test", (), {})
        assert StatefulObjectMeta.stateful_properties.__get__(object) == {}
        assert test_data.stateful_properties == {}
        assert type(test_data) is StatefulObjectMeta

    def test_metaclass(self):
        class TestClass(metaclass=StatefulObjectMeta):
            pass

        assert type(TestClass) is StatefulObjectMeta
        assert TestClass.stateful_properties == {}


class TestStatefulObject:
    def test_base(self):
        test_data = StatefulObject()
        assert not test_data.auto_commit
        assert not test_data.expired

        assert test_data.refresh(None) is None
        assert test_data.refresh("*") is None
        with raises(TypeError):
            test_data.refresh(1)
        with raises(TypeError):
            test_data.refresh(("param1", "param2", 1))

        assert test_data.commit(None) is None
        assert test_data.commit("*") is None
        with raises(TypeError):
            test_data.commit(1)
        with raises(TypeError):
            test_data.commit(("param1", "param2", 1))

    def test_inheritance(self):
        test_data = generate_stateful_object()
        assert test_data.expired
        assert test_data.auto_commit
        assert list(test_data.get_stateful_properties(None).keys()) == [
            "expired",
            "auto_commit",
        ]
        assert list(test_data.get_stateful_properties("*").keys()) == [
            "expired",
            "auto_commit",
        ]
        assert test_data.get_stateful_properties(
            ("expired", "auto_commit", "nonexistent")
        ) == {
            "expired": test_data.__class__.expired,
            "auto_commit": None,
            "nonexistent": None,
        }
        with raises(TypeError):
            test_data.commit(1)
        with raises(TypeError):
            test_data.commit(("param1", "param2", 1))

    def test_methods(self):
        test_data = generate_stateful_object()
        test_data.refresh("auto_commit")
        assert not test_data.auto_commit
        test_data.commit()
        assert test_data.auto_commit
        assert not test_data.expired
        test_data.refresh(("auto_commit", "expired"))
        assert test_data.expired
        assert not test_data.auto_commit
        test_data.commit("auto_commit")
        assert test_data.auto_commit
