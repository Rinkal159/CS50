from power import calPower

def test_power_negative():
    assert calPower(-2) == 4, "Power of -2 was not 4"
    assert calPower(-3) == 9, "Power of -3 was not 9"