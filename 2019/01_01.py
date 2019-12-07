"""
Day 1

amount of fuel for a module is based on mass
floor(mass / 3) - 2

12 -> 2
14 -> 2
1969 -> 654
100756 -> 33583

output:
sum of the fuel required for each module
"""
from utils import read_input


def calc_fuel(mass):
    """floor of the mass divided by 3 minus 2"""
    return (mass // 3) - 2


def tests():
    """tests from the description"""
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583


tests()

assert sum(calc_fuel(int(l)) for l in read_input(1)) == 3514064
