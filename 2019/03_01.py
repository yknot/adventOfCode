"""
Day 3

2 Wires

Find smallest L1 distance to the start where they cross
    
output:
Distance

"""
import math


def find_points(wire):
    x, y = 0, 0
    pts = []

    for i in wire:
        for j in range(int(i[1:])):
            if i[0] == "R":
                x += 1
            elif i[0] == "L":
                x -= 1
            elif i[0] == "U":
                y += 1
            elif i[0] == "D":
                y -= 1

            pts.append((x, y))

    return set(pts)


def find_min_cross(wire_a, wire_b):
    a_pts = find_points(wire_a)
    b_pts = find_points(wire_b)

    pts = a_pts.intersection(b_pts)
    min_sum = math.inf
    for x, y in pts:
        tmp_sum = abs(x) + abs(y)
        if tmp_sum < min_sum:
            min_sum = tmp_sum

    return min_sum


def split_input(inpt):
    wire_a, wire_b = inpt.split()
    wire_a = wire_a.split(",")
    wire_b = wire_b.split(",")

    return wire_a, wire_b


# run tests
def tests():
    assert (
        find_min_cross(
            *split_input(
                """R8,U5,L5,D3
U7,R6,D4,L4"""
            )
        )
        == 6
    )

    assert (
        find_min_cross(
            *split_input(
                """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
            )
        )
        == 159
    )

    assert (
        find_min_cross(
            *split_input(
                """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
            )
        )
        == 135
    )


tests()

print(find_min_cross(*split_input(open("03_input").read())))
