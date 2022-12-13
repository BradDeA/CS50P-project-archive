from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_hi():
    assert value('hi') == 20
    assert value('HI') == 20

def test_other_input():
    assert value('') == 100
    assert value('goodbye') == 100
    assert value('nope') == 100
    assert value('nothello') == 100
    assert value('123') == 100