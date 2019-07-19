from parser import *
import fabric

def test_parse():
    claim = parse('#123 @ 3,2: 5x4')

    assert claim.id == '123'
    assert claim.point.x == 3
    assert claim.point.y == 2
    assert claim.width == 5
    assert claim.height == 4
