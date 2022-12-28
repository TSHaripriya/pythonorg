import pytest

@pytest.mark.parametrize("a,b,c",[(1,2,3),(7,8,9)])
def test_functionadd(a,b,c):
    assert a+b == c

@pytest.mark.parametrize("a,b,c",[(3,2,1),(8,4,3)])
def test_functionsub(a,b,c):
    assert a-b==c
@pytest.mark.parametrize("a,b,c",[(3,2,1),(8,4,32)])
def test_functionmul(a,b,c):
    assert  a*b==c
