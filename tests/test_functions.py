import pytest

from calc_functions import add, subtract, multiply, divide

@pytest.mark.parametrize(
    ('x','y','ans'),
    [(1,2,3),
     (-1,2,1),
     (0,0,0)]
)
def test_add(x,y,ans):
    assert add(x, y) == ans

@pytest.mark.parametrize(
    ('x','y','ans'),
    [(1,2,-1),
     (-100,20,-120),
     (9,9,0)]
)
def test_subtract(x,y,ans):
    assert subtract(x, y) == ans

@pytest.mark.parametrize(
    ('x','y','ans'),
    [(2,3,6),
     (-1,20,-20),
     (9,0,0),
     (5,1,5)]
)
def test_multiply(x,y,ans):
    assert multiply(x, y) == ans

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 10) == 0
    assert divide(5, 0) == "ERROR"