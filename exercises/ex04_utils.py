"""Creates lists inside different functions."""
__author__ = "730673903"
same: bool = True


def all(actual_list: list[int], num: int) -> bool:
    """Checks if all the list has the same number as the given int."""
    index: int = 0
    # This first checks if the length of the list is 0 because if it is, there is nothing to compare the list to.
    if len(actual_list) == 0:
        return False
    # Only runs if the list has some numbers inside.
    else: 
        # runs through every index in the list
        while index < len(actual_list):
            if num == actual_list[index]:
                same = True
            else:
                return False
            index += 1
    return same


def max(actual_list: list[int]) -> int:
    """Returns the max value in the list."""
    # If there is nothing in the actual_list, it'll throw an error.
    if len(actual_list) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max = actual_list[0]
    # runs through every index in the list
    while index < len(actual_list):
        if actual_list[index] > max:
            max = actual_list[index]
        index += 1
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if both the lists are equal."""
    is_equal = True
    # it first checks if the lengths of the two lists are the same
    if len(list_one) != len(list_two):
        return False
    # if the lengths are the same, then the below code will run
    else:
        index: int = 0
        # runs through every index in the list
        while index < len(list_one):
            # checks if each value in both the lists are the same
            if list_one[index] == list_two[index]:
                is_equal = True
            else: 
                return False
            index += 1
        return is_equal
