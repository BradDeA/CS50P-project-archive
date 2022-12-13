from plates import is_valid

def main():
    test_valid_start()
    test_valid_empty()
    test_valid_number_check()
    test_valid_length()
    test_valid_alphanumeric()


def test_valid_start():
    assert is_valid('2A') == False
    assert is_valid('123456') == False
    assert is_valid('AA') == True

def test_valid_empty():
    assert is_valid('') == False

def test_valid_number_check():
    assert is_valid('AAA45A') == False
    assert is_valid('hj0000') == False

def test_valid_length():
    assert is_valid('hf453988') == False

def test_valid_alphanumeric():
    assert is_valid('df.453') == False

if __name__ == '__main__':
    main()
