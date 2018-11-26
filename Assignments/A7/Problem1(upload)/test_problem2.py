# Then, write the test for this function.Save this test as test_problem2.py
import problem2
def test_problem2():
    assert problem2.month_length("February", leap_year = False) == 28, 'failed on February in common year'
    assert problem2.month_length("February", leap_year = True) == 29, 'failed on February in leap year'
    assert problem2.month_length("March", leap_year = False) == 31, 'failed on March in common year'
    assert problem2.month_length("March", leap_year = True) == 31, 'failed on March in leap year'
    assert problem2.month_length("April", leap_year = False) == 30, 'failed on April in common year'
    assert problem2.month_length("April", leap_year = True) == 30, 'failed on April in leap year'