"""Combining two lists into a dictionary."""
__author__ = "730673903"


def zip(list_one: list[str], list_two: list[int]) -> dict[str, int]:
    """Takes two different lists and combines it into a dictionary."""
    zipped_dict: dict[str, int] = dict()
    if len(list_one) != len(list_two):
        return {}
    else:
        for index in range(len(list_one)):
            zipped_dict[list_one[index]] = list_two[index]
        return zipped_dict
    