from better_find_frequency_duplicate import *

def test_sum_frequencies():
    assert find_frequency_duplicate([1, -2, 3, 1]) == 2

def test_find_frequency_duplicate_no_frequency():
    assert find_frequency_duplicate([]) == None

def test_find_frequency_duplicate_no_duplicate():
    assert find_frequency_duplicate([1, 1, 1, 1]) == None
