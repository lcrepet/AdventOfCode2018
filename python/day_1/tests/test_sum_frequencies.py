from sum_frequencies import *

def test_sum_frequencies():
    assert sum_frequencies([1, -2, 3, 1]) == 3

def test_sum_no_frequency():
    assert sum_frequencies([]) == 0
