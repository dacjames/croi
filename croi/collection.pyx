import copy


def updated(dict left, dict right, join=lambda l, r: r):
    result = copy.copy(left)

    for k, v in right.iteritems():
        try:
            result[k] = join(left[k], v)
        except KeyError:
            result[k] = v

    return result
