import types

import croi

def test_memoized_function_unit():

    state = [0]

    @croi.memoized
    def function():
        state[0] = state[0] + 1
        return state[0]

    assert function() == 1
    assert function() == 1
    assert function() == 1


def test_memoized_function_largs():

    state = [0]

    @croi.memoized
    def function(x):
        state[0] = state[0] + x
        return state[0]

    assert function(1) == 1
    assert function(1) == 1

    state[0] = 0

    assert function(2) == 2
    assert function(2) == 2


def test_memoized_function_largs():

    state = [0]

    @croi.memoized
    def function(x, y=None):
        state[0] = state[0] + x + y
        return state[0]

    assert function(1, y=0) == 1
    assert function(1, y=0) == 1

    state[0] = 0

    assert function(1, y=1) == 2
    assert function(1, y=1) == 2


def test_memoized_method():
    class Test(object):
        def __init__(self):
            self.state = 0

        @croi.memoized
        def foo(self, x):
            self.state += x
            return self.state


    t = Test()
    u = Test()

    assert t.foo(1) == 1
    assert t.foo(1) == 1

    assert u.foo(2) == 2
    assert u.foo(2) == 2


def test_memoized_property():
    class Foo(object):
        def __init__(self):
            self.state = 0

        @croi.memoized_property
        def bar(self):
            self.state += 1
            return self.state

    f = Foo()

    assert f.bar == 1
    assert f.bar == 1



