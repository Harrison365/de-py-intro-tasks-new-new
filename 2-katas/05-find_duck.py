def find_duck():
    pass

# tests


def test_finds_lonesome_duck():
    expected = 1
    result = find_duck('🦆')

    assert result == expected


def test_finds_duck_in_the_queue():
    expected = 3
    result = find_duck('🐄 🐖 🦆 🐑 🦙')

    assert result == expected


def test_handles_non_existant_duck():
    expected = -1
    result = find_duck('🐄 🐖 🐑 🦙')

    assert result == expected
