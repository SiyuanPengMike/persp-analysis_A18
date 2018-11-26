#Then, write the test for this function.Save this test as test_problem2.py
import pytest
import problem3
def test_problem3():
    assert problem3.operate(2,7,"+") == 9, 'failed on add function'
    assert problem3.operate(2,7,"-") == -5, 'failed on subtract function'
    assert problem3.operate(2,7,"*") == 14, 'failed on multiply function'
    assert problem3.operate(4,2,"/") == 2, 'failed on division function'
    pytest.raises(TypeError, problem3.operate, a=2, b=7, oper=2.7)
    pytest.raises(ZeroDivisionError, problem3.operate, a=2, b=0, oper='/')
    pytest.raises(ValueError, problem3.operate, a=2, b=7, oper="^")