def multiply_by_5(x):
    return x * 5


# tests
def test_returns_zero_when_passed_zero():
    expected = 0
    result = multiply_by_5(0)

    assert result == expected


def test_multiplies_passed_arg_by_five():
    assert multiply_by_5(10) == 50
    assert multiply_by_5(7) == 35
