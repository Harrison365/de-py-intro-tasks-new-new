def measure_words():
    pass


#tests
def test_returns_empty_dict_when_passed_empty_str():
    expected = {}
    result = measure_words('')

    assert result == expected

def test_assigns_property_for_single_word():
    expected = {'hello': 5}
    result = measure_words('hello')

    assert result == expected

def test_assigns_property_for_multiple_words():
    expected = {'multiple': 8, 'words': 5, 'are': 3, 'fun': 3}
    result = measure_words('multiple, words, are, fun')

    assert result == expected
