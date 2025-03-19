from lib import to_test
from lib import numpy_vect


def test_to_test():
    assert to_test(5) == 6


def test_numpy():
    assert numpy_vect().sum() == 6
