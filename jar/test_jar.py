from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == '🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(4)