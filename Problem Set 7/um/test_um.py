from um import count

def main():
    test_correct()
    test_word()
    test_extra_m()

def test_correct():
    assert count('Um, thanks, um...') == 2

def test_word():
    assert count('Um, thanks for the album.') == 1

def test_extra_m():
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2

if __name__ == '__main__':
    main()