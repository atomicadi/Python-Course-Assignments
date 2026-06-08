# copied from Day04 and edited by Aditya Barman, Date: June 07, 2026; @weizmann

from logic import calc_q_trans


def test_valid_input():

    q_trans, error = calc_q_trans("5", "0", "300", "1")

    assert error is None
    assert q_trans is not None


def test_invalid_mass():

    q_trans, error = calc_q_trans("abc", "0", "300", "1")

    assert q_trans is None
    assert error is not None


def test_invalid_TC():

    q_trans, error = calc_q_trans("5", "n", "300", "1")

    assert q_trans is None
    assert error is not None


def test_invalid_temperature():

    q_trans, error = calc_q_trans("5", "0", "abc", "1")

    assert q_trans is None
    assert error is not None


def test_invalid_volume():

    q_trans, error = calc_q_trans("5", "0", "300", "abc")

    assert q_trans is None
    assert error is not None
