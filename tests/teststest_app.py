from app import add

def test_positive_numbers():
    assert add(2, 3) == 5

def test_zero():
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 10) == 5

def test_large_numbers():
    assert add(1000, 2000) == 3000