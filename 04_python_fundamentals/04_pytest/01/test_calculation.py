import calculation

def test_add():
    assert calculation.add(1, 2) == 3
    assert calculation.add(0, 0) == 0
    assert calculation.add(-1, 1) == 0

def test_multiply():
    assert calculation.multiply(1, 2) == 2
    assert calculation.multiply(0, 0) == 0
    assert calculation.multiply(-1, 1) == -1    