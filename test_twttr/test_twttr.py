from twttr import shorten

def test_shorten_normal():
    assert shorten('hello') == 'hll'

def test_shorten_capital():
    assert shorten('HELLO') == 'HLL'

def test_shorten_alternating():
    assert shorten('HeLlO') == 'HLl'
    assert shorten('hElLo') == 'hlL'

def test_shorten_punctuation():
    assert shorten('hel.lo') == 'hl.l'
    assert shorten('HEL.LO') == 'HL.L'

def test_shorten_numbers():
    assert shorten('h3ll0') == 'h3ll0'