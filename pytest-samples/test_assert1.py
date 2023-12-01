import pytest

# Test cases to check asseriotns
def f():
    return 3

def test_function():
    assert f()== 4 , "Incorrect value"

def test_zero_divtion():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        
        f()
    assert "maximum recursion" in str(excinfo)