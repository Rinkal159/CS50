from power import calPower

def test_power_zero():
    assert calPower(0) == 0, "Power of 0 was not 0"