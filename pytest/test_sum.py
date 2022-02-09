from sum import sum

def test_sum():
    assert sum(1, 2) == 3

def test_sum_bad():
    assert sum(1, 2) != 4
