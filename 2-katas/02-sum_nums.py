def sum_nums(*nums):
    return sum(nums)


# tests
def test_sums_single_number():
    expected = 1
    result = sum_nums(1)

    assert result == expected


def test_sums_two_numbers():
    expected = 3
    result = sum_nums(1, 2)

    assert result == expected


def test_sums_multiple_numbers():
    expected = 8
    result = sum_nums(-1, 2, 3, 4)

    assert result == expected
