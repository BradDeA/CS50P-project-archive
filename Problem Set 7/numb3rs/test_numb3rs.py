from numb3rs import validate

def main():
    test_one()
    test_two()

def test_one():
    assert validate('1.2.3.4') == True
    assert validate('1') == False


def test_two():
    assert validate('1.345.222.8') == False



if __name__ == '__main__':
    main()