from pytest import raises

from stateful.property import stateful_property

from .util import PropertyOwner, generate_test_functions


class TestConstructor:
    def test_noparam(self):
        test_data = stateful_property()
        assert test_data.fget is None
        assert test_data.fset is None
        assert test_data.fdel is None
        assert test_data.frefresh is None
        assert test_data.refresh == test_data.fallback_refresh
        assert test_data.fcommit is None
        assert test_data.commit == test_data.fallback_commit
        assert test_data.auto_commit is None

    def test_parameterized_no_autocommit(self):
        _, functions = generate_test_functions()
        test_data = stateful_property(*functions)
        assert test_data.fget is functions[0]
        assert test_data.fset is functions[1]
        assert test_data.fdel is functions[2]
        assert test_data.frefresh is functions[3]
        assert test_data.refresh is functions[3]
        assert test_data.fcommit is functions[4]
        assert test_data.commit is functions[4]
        assert test_data.auto_commit is None

    def test_parameterized_autocommit(self):
        test_data = stateful_property(auto_commit=True)
        assert test_data.auto_commit is True


class TestMethods:
    def test_functions(self):
        comparator, functions = generate_test_functions()
        test_data = stateful_property(*functions)
        test_data.fget(0)
        test_data.fset(0, 1)
        test_data.fdel(0, 1, 2)
        test_data.refresh(0, 1, 2, 3)
        test_data.commit(0, 1, 2, 3, 4)
        assert comparator == [1, 2, 3, 4, 5]

    def test_descriptors_no_autocommit(self):
        comparator, functions = generate_test_functions()
        test_data = stateful_property(*functions, None)
        owner = PropertyOwner()

        test_data.__get__(owner)
        assert comparator[0] == 1
        assert comparator[3] == 0

        owner.expired = True
        test_data.__get__(owner)
        assert comparator[0] == 2
        assert comparator[3] == 1

        test_data.__set__(owner, None)
        assert comparator[1] == 2
        assert comparator[4] == 0
        test_data.__delete__(owner)
        assert comparator[2] == 1
        assert comparator[4] == 0

        test_data.auto_commit = True
        test_data.__set__(owner, None)
        assert comparator[1] == 4
        assert comparator[4] == 1
        test_data.__delete__(owner)
        assert comparator[2] == 2
        assert comparator[4] == 2

    def test_descriptors_autocommit(self):
        comparator, functions = generate_test_functions()
        test_data = stateful_property(*functions, True)
        owner = PropertyOwner()

        test_data.__get__(owner)
        assert comparator[0] == 1
        assert comparator[3] == 0

        owner.expired = True
        test_data.__get__(owner)
        assert comparator[0] == 2
        assert comparator[3] == 1

        test_data.__set__(owner, None)
        assert comparator[1] == 2
        assert comparator[4] == 1
        test_data.__delete__(owner)
        assert comparator[2] == 1
        assert comparator[4] == 2


class TestDecorator:
    def test_noparam(self):
        @stateful_property
        def test_data(*args):
            return len(args)

        owner = PropertyOwner()
        assert test_data.fget() == 0
        assert test_data.__get__(owner) == 1
        assert test_data.fset is None
        assert test_data.fdel is None
        assert test_data.refresh == test_data.fallback_refresh
        assert test_data.commit == test_data.fallback_commit
        assert test_data.auto_commit is None

    def test_parameterized(self):
        @stateful_property(auto_commit=True)
        def test_data(*args):
            return len(args)

    def test_descriptors(self):
        comparator, functions = generate_test_functions()

        @stateful_property()
        def test_data(*args):
            return functions[0](*args)

        @test_data.setter
        def test_data(*args):
            return functions[1](*args)

        @test_data.deleter
        def test_data(*args):
            return functions[2](*args)

        @test_data.refresher
        def test_data(*args):
            return functions[3](*args)

        @test_data.committer
        def test_data(*args):
            return functions[4](*args)

        owner = PropertyOwner(True, True)
        test_data.__get__(owner)
        test_data.__set__(owner, None)
        test_data.__delete__(owner)
        assert comparator == [1, 2, 1, 1, 2]
