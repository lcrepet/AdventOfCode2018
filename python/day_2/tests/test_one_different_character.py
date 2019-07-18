from one_different_character import *

def test_find_uniq_difference_between():
    assert find_uniq_difference_between('aba', 'aaa') == 1

def test_find_uniq_difference_between_different_size():
    assert find_uniq_difference_between('aba', 'abaa') == None

def test_find_uniq_difference_between_identical_ids():
    assert find_uniq_difference_between('aba', 'aba') == None

def find_uniq_difference_between_totally_different_ids():
    assert find_uniq_difference_between('abc', 'defgh') == None

def find_uniq_difference_between_anagrams():
    assert find_uniq_difference_between('abc', 'bca') == None

def test_find_common_characters_in_close_ids():
    ids = ['abcde',
           'fghij',
           'klmno',
           'pqrst',
           'fguij',
           'axcye',
           'wvxyz']

    assert find_common_characters_in_close_ids(ids) == 'fgij'

def test_find_common_characters_in_close_ids_with_no_id():
    assert find_common_characters_in_close_ids([]) == None

def test_find_common_characters_in_close_ids_with_one_id():
    assert find_common_characters_in_close_ids(['abcde']) == None

def test_find_common_characters_in_close_ids_with_totally_different_ids():
    ids = ['abcde',
           'fghij',
           'klmno',
           'pqrst',
           'axcye',
           'wvxyz']

    assert find_common_characters_in_close_ids([]) == None

def test_find_common_characters_in_close_ids_with_identical_ids():
    ids = ['abcde',
           'abcde',
           'abcde']

    assert find_common_characters_in_close_ids([]) == None



