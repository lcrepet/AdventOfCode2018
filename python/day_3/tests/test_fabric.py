from fabric import *

def test_print_on():
    plan = [['', '', '', '0', ''],
            ['', '', '', '0', ''],
            ['', '', '', '0', ''],
            ['', '', '', '0', ''],
            ['', '', '', '0', '']]

    claim = Claim('1', 1, 1, 3, 3)

    assert claim.print_on(plan) == 3
    assert claim.is_overlapped
    assert plan[1][3] == 'X'
    assert plan[2][3] == 'X'
    assert plan[3][3] == 'X'

def test_print_on_no_overlapped_claim():
    plan = [['', '', '', '', '0'],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']]

    claim = Claim('1', 1, 1, 3, 3)

    assert claim.print_on(plan) == 0
    assert not(claim.is_overlapped)

def test_print_on_plan_with_already_overlapped_claims():
    plan = [['', '', 'X', '0', ''],
            ['', '', 'X', '0', ''],
            ['', '', 'X', 'X', ''],
            ['', '', 'X', '0', ''],
            ['', '', 'X', '0', '']]

    claim = Claim('1', 1, 1, 3, 3)

    assert claim.print_on(plan) == 2
    assert claim.is_overlapped

def test_is_overlapped():
    plan = [['', '', 'X', '0', ''],
            ['', '', 'X', 'X', ''],
            ['', '', 'X', 'X', ''],
            ['', '', 'X', 'X', ''],
            ['', '', 'X', '0', '']]

    claim = Claim('1', 1, 1, 3, 3)

    assert claim.check_if_overlapped_on(plan)

def test_is_overlapped_no_overlapped_claim():
    plan = [['', '', '', '', '0'],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']]

    claim = Claim('1', 1, 1, 3, 3)

    assert not(claim.check_if_overlapped_on(plan))

