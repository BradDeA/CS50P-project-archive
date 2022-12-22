from project import *
import pytest

def test_request():
    assert request() == 'y'

def test_resizer():
    with pytest.raises(ImgError):
       resizer('','')

def test_tkinter_window():
    assert tkinter_window() == 'running'
