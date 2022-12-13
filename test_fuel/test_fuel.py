from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('6/0')
    with pytest.raises(ValueError):
        convert('a/b')
        convert('a/9')
        convert('4/f')

    assert convert('1/2') == 50

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'