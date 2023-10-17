def get_length(str):
    for letter in str:
        if letter == " ":
            str = str.replace(letter, "")
    return len(str)


# ALTERNATIVE SOLUTION
# def get_length(str):
#     new_str = ""
#     for letter in str:
#         if letter != " ":
#             new_str += letter
#     return len(new_str)


# tests


def test_measures_the_length_of_single_char():
    expected = 1
    result = get_length("a")

    assert result == expected


def test_measures_the_length_of_single_word():
    expected = 4
    result = get_length("tofu")

    assert result == expected


def test_ignores_white_spaces():
    expected = 22
    result = get_length("Linda McCartney sausages")

    assert result == expected
