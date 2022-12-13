from seasons import minutes, format_check
import pytest

def main():
    test_format()
    test_minutes()

def test_format():
    assert format_check('1999-01-01') == True
    with pytest.raises(SystemExit):
        format_check('January 4th, 2000')

def test_minutes():
    assert minutes(['1999', '01', '01']) == 'Twelve million, five hundred seventy-four thousand eighty minutes'

if __name__ == '__main__':
    main()