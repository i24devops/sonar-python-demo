from app.calculator import add, divide, is_even, duplicate_logic

def test_add():
    assert add(2, 3) == 5

def test_divide_ok():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(1, 0) is None

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_duplicate_logic():
    assert duplicate_logic(12) == "BIG"
    assert duplicate_logic(7) == "MID"
    assert duplicate_logic(2) == "SMALL"
