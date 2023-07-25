def contains_repeats():
    pass


# tests
def test_returns_false_for_single_character():
    expected = False
    result = contains_repeats('a')

    assert result == expected


def test_returns_false_for_unique_characters():
    expected = False
    result = contains_repeats('abcde')

    assert result == expected


def test_detects_multiple_characters():
    expected = True
    result = contains_repeats('aabccdde')

    assert result == expected
