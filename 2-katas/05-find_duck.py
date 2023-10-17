def find_duck(str):
    arr = str.split(" ")
    for i in range(len(arr)):
        if arr[i] == "🦆":
            return i + 1
    return -1


# alt using index of
def find_duck(str):
    arr = str.split(" ")
    if "🦆" in arr:
        return arr.index("🦆") + 1
    else:
        return -1


# tests


def test_finds_lonesome_duck():
    expected = 1
    result = find_duck("🦆")

    assert result == expected


def test_finds_duck_in_the_queue():
    expected = 3
    result = find_duck("🐄 🐖 🦆 🐑 🦙")

    assert result == expected


def test_handles_non_existant_duck():
    expected = -1
    result = find_duck("🐄 🐖 🐑 🦙")

    assert result == expected
