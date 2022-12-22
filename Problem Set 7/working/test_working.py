from working import convert
import pytest

def main():
    test_correct()
    test_omit()
    test_minute()
    test_invalid_format()

def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_omit():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_invalid_format():
    with pytest.raises(ValueError):
        convert('9AM to 5PM')

if __name__ == '__main__':
    main()