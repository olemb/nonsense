def xor_operator(a, b):
    return a ^ b


def xor_mod(a, b):
    return (a + b) % 2


def xor_compare(a, b):
    return int(a != b)


def xor_lookup_dict(a, b):
    return {
        (0, 0): False,
        (0, 1): True,
        (1, 0): True,
        (1, 1): False,
        }[(a, b)]


def xor_lookup_set(a, b):
    return int((a, b) in {(0, 1), (1, 0)})


def xor_count_with_set(a, b):
    return int(len({a, b}) == 2)


def xor_add(a, b):
    return int(a + b == 1)


def xor_sum(a, b):
    return int(sum([a, b]) == 1)


def xor_substring(a, b):
    return int('{}{}'.format(a, b) in "10 01")


def xor_array(a, b):
    return [0, 1, 1, 0][a << 1 | b]


def xor_or_and(a, b):
    return int(a | b and not a & b)


def xor_sort(a, b):
    return int(sorted([a, b]) == [0, 1])


def xor_balance(a, b):
    return int(a - b != 0)


def find_functions():
    for name in sorted(globals()):
        if name.startswith('xor_'):
            yield globals()[name]


def test_function(xor):
    return all([xor(0, 0) == xor(1, 1) == 0,
                xor(1, 0) == xor(0, 1) == 1])


def test_all():
    for func in find_functions():
        if test_function(func):
            print('OK: {}()'.format(func.__name__))
        else:
            print('FAILED: {}()'.format(func.__name__))


test_all()
