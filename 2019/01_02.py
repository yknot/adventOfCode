"""
Day 1 part 2

amount of fuel for a module is based on mass
floor(mass / 3) - 2

part 2: we need to calculate fuel for the fuel...
as long as the calculated fuel is not negative 
  (aka the floor doesen't amount to 2 or less)
then we need to add the new fuel

test cases
12 -> 2
14 -> 2
1969 -> 654 + 216 + 70 + 21 + 5 = 966
100756 -> 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346

output:
sum of the fuel required for each module
"""


def calc_fuel(mass):
    """floor of the mass divided by 3 minus 2"""
    fuel = (mass // 3) - 2
    # check if added fuel is less than 0
    if fuel <= 0:
        return 0
    # otherwise recurse to add the fuel for our fuel
    return fuel + calc_fuel(fuel)


def tests():
    """tests from the description"""
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 966
    assert calc_fuel(100756) == 50346


tests()

assert sum(calc_fuel(int(l)) for l in open("01_input").readlines()) == 5268207
