from lib import numpy_vect, to_test


def test_to_test() -> None:
    assert to_test(5) == 6


def test_numpy() -> None:
    assert numpy_vect().sum() == 6
