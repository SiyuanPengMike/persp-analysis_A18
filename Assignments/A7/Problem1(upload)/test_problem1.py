import problem1
def test_problem1():
    assert problem1.smallest_factor(2) == 2, 'failed on 2'
    assert problem1.smallest_factor(3) == 3, 'failed on 3'
    assert problem1.smallest_factor(4) == 2, 'failed on 4'
    assert problem1.smallest_factor(9) == 3, 'failed on 9'
    assert problem1.smallest_factor(13) == 13, 'failed on 13'