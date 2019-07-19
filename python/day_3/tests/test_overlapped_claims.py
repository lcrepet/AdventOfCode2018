from overlapped_claims import *
import fabric

def test_count_overlapped_claims():
    claims = [fabric.Claim('1', 1, 3, 4, 4),
              fabric.Claim('2', 3, 1, 4, 4),
              fabric.Claim('3', 5, 5, 2, 2)]

    assert count_overlapped_claims(claims, 7, 7) == 4

def test_count_overlapped_claims_with_no_claim():
    assert count_overlapped_claims([], 0, 0) == 0
