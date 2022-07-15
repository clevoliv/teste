from twttr import shorten


def test_shorten():
    assert shorten('ABRACADABRA') == 'BRCDBR'
    assert shorten('CACHORRO') == 'CCHRR'
    assert shorten('maluco') == 'mlc'
    assert shorten('aaaiii7oouu') == '7'
    assert shorten('aaaiiioouu') == ''
    assert shorten('aaaii.io,ouu') == '.,'