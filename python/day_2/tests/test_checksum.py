from checksum import *

def test_checksum():
    ids = ['abcdef',
           'bababc',
           'abbcde',
           'abcccd',
           'aabcdd',
           'abcdee',
           'ababab']

    assert checksum(ids) == 12

def test_checksum_no_id():
    assert checksum([]) == 0
