# Writtenn by Aditya Barman; May 03, 2026 @weizmann
# checking the calc algorithm using pytest

from Calc_q_trans_library import calc_q_trans

def test_valid_input():
    # Valid inputs
    q_trans, error = calc_q_trans("5", "300", "1")
    
    assert error is None
    assert q_trans is not None


def test_invalid_mass():
    # Non-numeric mass
    q_trans, error = calc_q_trans("a", "300", "1")
    
    assert q_trans is None
    assert "mass" in error


def test_invalid_temperature():
    # Non-numeric temperature
    q_trans, error = calc_q_trans("5", "mnp", "1")
    
    assert q_trans is None
    assert "temperature" in error


def test_invalid_volume():
    # Non-numeric volume
    q_trans, error = calc_q_trans("5", "300", "xyz")
    
    assert q_trans is None
    assert "volume" in error

def test_negative_input():
    # Negative values should fail (because .isdigit() rejects "-5")
    q_trans, error = calc_q_trans("-5", "300", "1")
    
    assert q_trans is None
    assert error is not None
