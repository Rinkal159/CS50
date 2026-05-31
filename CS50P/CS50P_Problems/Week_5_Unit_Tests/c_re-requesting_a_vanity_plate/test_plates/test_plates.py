from plates import is_valid

def test_beginning_alphabets():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False
    assert is_valid("1S345") == False 
    assert is_valid("C1345") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("CS52345") == False

def test_numbersInMiddle():
    assert is_valid("AAZZ22") == True
    assert is_valid("AA22ZZ") == False
    assert is_valid("AAZZ02") == False

def test_onlyAlphaAndNumbers():
    assert is_valid("AABBCC") == True
    assert is_valid("AA??") == False
    assert is_valid(".?!,") == False
