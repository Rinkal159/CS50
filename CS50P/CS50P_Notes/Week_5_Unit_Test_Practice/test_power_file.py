from power import calPower

def test_power():
    assert calPower(2) == 4, "Power of 2 was not 4" #condition must be true, if it is false then the AssertionError next to comma will raise
    assert calPower(3) == 9, "Power of 3 was not 9"
    
# run pytest test_power.py to run the tests
# a function containing 5 test cases, and if the 2nd test case fails then the remaining 3 test cases will not be tested in the same runtime, after that test case is resolved then only after rest will excute.