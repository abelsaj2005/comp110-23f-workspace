"""Test my zip function"""
__author__ = "730673903"

from lessons.zip import zip


def test_empty_list():
    """Testing on empty lists."""
    assert zip([], []) == {}


def test_different_lengths():
    """Testing on two lists with different lengths."""
    test_list_one = ["Sunday", "Monday", "Tuesday"]
    test_list_two = [1, 2]
    assert zip(test_list_one, test_list_two) == {}


def test_two_list_same_length():
    """Testing on two lists with the same length."""
    test_list_one = ["Happy", "Tuesday"]
    test_list_two = [1, 2]
    assert zip(test_list_one, test_list_two) == {"Happy": 1, "Tuesday":2}