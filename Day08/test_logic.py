from logic import calc_q_trans


def test_valid_input():

    q_trans, error = calc_q_trans("5", "300", "1")

    assert error is None
    assert q_trans is not None


def test_invalid_mass():

    q_trans, error = calc_q_trans("abc", "300", "1")

    assert q_trans is None
    assert error is not None


def test_invalid_temperature():

    q_trans, error = calc_q_trans("5", "abc", "1")

    assert q_trans is None
    assert error is not None


def test_invalid_volume():

    q_trans, error = calc_q_trans("5", "300", "abc")

    assert q_trans is None
    assert error is not None
