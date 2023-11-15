"""Summing the elements of a list using different loops."""
__author__ = "730673903"


def w_sum(vals: list[float]) -> float:
    """Sums up the values in the list using a while loop."""
    idx = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums up the values in the list using a for loop."""
    sum: float = 0.0
    for item in vals:
        sum += item
    return sum
     

def f_range_sum(vals: list[float]) -> float:
    """Sums up the values in the list using a for ... in range loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum