from twttr import shorten

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("KAREENA") == "KRN"

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("kareena") == "krn"

def test_shorten_mixcase():
    assert shorten("TWitTEr") == "TWtTr"
    assert shorten("KArEEnA") == "Krn"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"

def test_empty():
    assert shorten("") == ""
