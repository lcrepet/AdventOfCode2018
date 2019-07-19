from only_intact_claim import *
import fabric

def test_find_only_not_overlapped_claim():
    claims = [fabric.Claim('1', 1, 3, 4, 4),
              fabric.Claim('2', 3, 1, 4, 4),
              fabric.Claim('3', 5, 5, 2, 2)]

    not_overlapped_claim = find_only_not_overlapped_claim(claims, 7, 7)

    assert not_overlapped_claim
    assert not_overlapped_claim.id == '3'

def test_find_only_not_overlapped_claim_with_no_claim():
    not_overlapped_claim = find_only_not_overlapped_claim([], 0, 0)

    assert not(not_overlapped_claim)

def test_find_only_not_overlapped_claim_with_no_solution():
    claims = [fabric.Claim('1', 1, 3, 4, 4),
              fabric.Claim('2', 3, 1, 4, 4),
              fabric.Claim('3', 4, 5, 2, 2)]

    not_overlapped_claim = find_only_not_overlapped_claim(claims, 7, 7)

    assert not(not_overlapped_claim)

def test_find_only_not_overlapped_claim_with_multiple_solutions():
    claims = [fabric.Claim('1', 1, 3, 4, 4),
              fabric.Claim('2', 3, 1, 2, 2),
              fabric.Claim('3', 5, 5, 2, 2)]

    not_overlapped_claim = find_only_not_overlapped_claim(claims, 7, 7)

    assert not_overlapped_claim
    assert not_overlapped_claim.id == '1'
