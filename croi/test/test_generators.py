import croi


def test_forever():
    forever_up = croi.forever()

    for i, x in enumerate(forever_up):
        assert i == x
        if i >= 10:
            break

    assert i == 10

    forever_down = croi.forever(step=-1)

    for i, x in enumerate(forever_down):
        assert i == -x
        if i >= 10:
            break

    assert i == 10

    forever_step = croi.forever(initial=10, step=2)

    for i, x in enumerate(forever_step):
        assert i * 2 + 10 == x
        if i >= 10:
            break

    assert i == 10


def test_build():
    state = [0]

    def factory():
        state[0] = state[0] + 1
        return state[0]

    for i, x in enumerate(croi.build(factory)):
        assert i + 1 == x
        if i >= 10:
            break

    assert i == 10


def test_duplicate():

    for i, x in enumerate(croi.duplicate(1)):
        assert x == 1
        if i >= 10:
            break

    assert i == 10


def test_zeros():
    for i, x in enumerate(croi.zeros()):
        assert x == 0
        if i >= 10:
            break

    assert i == 10


def test_ones():
    for i, x in enumerate(croi.ones()):
        assert x == 1
        if i >= 10:
            break

    assert i == 10


def test_randoms():
    for i, x in enumerate(croi.random_ints()):
        assert 0 <= x <= 1
        if i >= 10:
            break

    assert i == 10

    for i, x in enumerate(croi.random_ints(0, 10)):
        assert 0 <= x <= 10
        if i >= 100:
            break

    assert i == 100

    for i, x in enumerate(croi.random_floats(-1, 1)):
        assert -1 <= x <= 1
        if i >= 100:
            break

    assert i == 100


def test_take():
    result = list(croi.take(10, croi.forever()))
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == result

    result = list(croi.take(lambda x: x < 3, croi.forever()))
    assert [0, 1, 2] == result


def test_drop():
    result = list(croi.drop(5, range(10)))
    assert [5, 6, 7, 8, 9] == result

    result = list(croi.drop(lambda x: x < 3, range(10)))
    assert [3, 4, 5, 6, 7, 8, 9] == result


def test_nth():
    assert 5 == croi.nth(5, croi.forever(1))


def test_head():
    assert 0 == croi.head(croi.forever())


def test_tail():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == list(croi.tail(range(10)))


def test_select():
    result = list(croi.select(1, [1, 2, 1, 4]))
    assert [1, 1] == result

    result = list(croi.select(lambda x: x % 2 == 0, range(10)))
    assert [0, 2, 4, 6, 8] == result

    result = list(croi.select(r'a{1,3}$', ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
    assert ['a', 'aa', 'aaa'] == result


def test_reject():
    result = list(croi.reject(1, [1, 2, 1, 4]))
    assert [2, 4] == result

    result = list(croi.reject(lambda x: x % 2 == 0, range(10)))
    assert [1, 3, 5, 7, 9] == result

    result = list(croi.reject(r'a{1,3}$', ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
    assert ['', 'aaaa', 'aaaaa'] == result
