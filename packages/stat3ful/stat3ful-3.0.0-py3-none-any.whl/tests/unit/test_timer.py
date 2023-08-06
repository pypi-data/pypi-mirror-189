from datetime import datetime, timedelta
from time import sleep

from pytest import raises

from stateful.timer import (TimedExpirationMixin, TimedExpirationMixinMeta,
                            Timer)

from .util import TimerEmulator


class TestTimer:
    def test_invalid_data(self):
        with raises(TypeError):
            test_data = Timer(invalid_arg=1, seconds=1)
        with raises(TypeError):
            test_data = Timer(seconds=1, minutes=None)
        with raises(TypeError):
            test_data = Timer(seconds="1")

    def test_valid_data(self):
        test_data = Timer(seconds=5)
        assert iter(test_data) is test_data
        timestamp = next(test_data)
        assert datetime.now() + timedelta(seconds=5) >= timestamp


class TestTimedExpirationMixinMeta:
    def test_base(self):
        assert TimedExpirationMixinMeta.__prepare__("test", ()) == {"__tclass__": Timer}
        assert TimedExpirationMixinMeta.__prepare__("test", (), timer_class=None) == {
            "__tclass__": None
        }
        test_data = TimerEmulator()
        refresher = TimedExpirationMixinMeta.refresh_decorator(TimerEmulator.refresh)
        refresher(test_data)
        assert test_data._expires == 0
        assert test_data.access_counter == 1
        TestClass = TimedExpirationMixinMeta(
            "test", (TimerEmulator,), dict(TimerEmulator.__dict__)
        )
        assert TestClass.refresh != TimerEmulator.refresh

    def test_metaclass(self):
        class TestClass(metaclass=TimedExpirationMixinMeta, timer_class=None):
            def __init__(self):
                self._iter = 0

            @property
            def timer(self):
                return iter(lambda: self._iter, None)

            def refresh(self, spec=None):
                self._iter += 1

        assert TestClass.__tclass__ is None
        test_data = TestClass()
        test_data.refresh()
        assert test_data._expires == 1


class TestTimedExpirationMixin:
    def test_timer(self):
        test_data = TimedExpirationMixin()
        assert test_data.timer is None
        test_data.timer = {"seconds": 5}
        assert test_data._expires >= datetime.now()
        assert datetime.now() + timedelta(seconds=5) >= test_data._expires
        test_data.timer = None
        assert test_data.timer is None

    def test_expiration(self):
        test_data = TimedExpirationMixin()
        assert not test_data.expired
        test_data.timer = {"seconds": 5}
        assert not test_data.expired
        sleep(5)
        assert test_data.expired

    def test_mixin(self):
        class TestClass(TimedExpirationMixin):
            def __init__(self):
                self.timer = {"seconds": 5}

            def refresh(self, spec=None):
                pass

        test_data = TestClass()
        sleep(5)
        assert test_data.expired
        test_data.refresh()
        assert not test_data.expired
