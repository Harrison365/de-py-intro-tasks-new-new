def contains_digit(num):
    result = []
    for i in range(1, 101):
        if str(num) in str(i):
            result.append(i)
    return result


# tests


def test_evaluates_numerals_units_position():
    expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = contains_digit(0)

    assert result == expected


def test_evaluates_numerals_all_positions():
    expected = [
        9,
        19,
        29,
        39,
        49,
        59,
        69,
        79,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
    ]
    result = contains_digit(9)

    assert result == expected
