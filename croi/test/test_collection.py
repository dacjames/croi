import croi


def test_updated_default():
    x = {'a': 1, 'b': 2}
    y = {'a': 10, 'c': 30}

    z0 = croi.updated(x, y)
    z1 = croi.updated(y, x)

    assert z0 == {'a': 10, 'b': 2, 'c': 30}
    assert z1 == {'a': 1, 'b': 2, 'c': 30}

    x['a'] = -1

    assert z0 == {'a': 10, 'b': 2, 'c': 30}
    assert z1 == {'a': 1, 'b': 2, 'c': 30}


def test_updated_custom():
    x = {'a': 1, 'b': 2}
    y = {'a': 10, 'c': 30}

    z0 = croi.updated(x, y, join=lambda l, r: l + r)
    z1 = croi.updated(y, x, join=lambda l, r: l - r)

    assert z0 == {'a': 11, 'b': 2, 'c': 30}
    assert z1 == {'a': 9, 'b': 2, 'c': 30}
