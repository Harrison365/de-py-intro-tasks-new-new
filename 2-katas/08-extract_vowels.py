def extract_vowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for char in str:
        if char in vowels:
            result += char
    return result


# tests
def test_returns_empty_string_whn_no_vowels_found():
    expected = ""
    result = extract_vowels("rhythm")

    assert result == expected


def test_returns_single_voweled_str():
    expected = "a"
    result = extract_vowels("a")

    assert result == expected


def test_returns_muliple_vowels_in_string():
    expected = "ae"
    result = extract_vowels("apple")

    assert result == expected


def test_antelopes_are_fun():
    expected = "aeoe"
    result = extract_vowels("antelope")

    assert result == expected
