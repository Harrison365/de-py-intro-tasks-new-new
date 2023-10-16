def is_square_num(num):
    root = int(num**0.5)
    return root * root == num


# tests
def test_reports_when_not_square_number():
    assert is_square_num(2) == False
    assert is_square_num(5) == False
    assert is_square_num(12) == False


def test_reports_when_square_number():
    assert is_square_num(1) == True
    assert is_square_num(9) == True
    assert is_square_num(25) == True
