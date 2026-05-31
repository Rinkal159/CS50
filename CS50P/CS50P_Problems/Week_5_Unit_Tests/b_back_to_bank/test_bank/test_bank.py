from bank import value

def test_greeting_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("HeLlO") == 0
    assert value("hello, John") == 0
    assert value("      HELLO      ") == 0

def test_greeting_h():
    assert value("hi") == 20
    assert value("hola") == 20
    assert value("hi, fellow") == 20
    assert value("      HI      ") == 20

def test_greeting_other():
    assert value("namaste") == 100
    assert value("KEM CHHO") == 100
    assert value("????") == 100
    assert value("123HELLO") == 100
    assert value("") == 100
