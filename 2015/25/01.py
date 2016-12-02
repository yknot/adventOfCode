def next_val(c):
    return c * 252533 % 33554393


position = [2947, 3029]
# position = [6, 6]

loc = [1, 1]
next_row = 2
current = 20151125
while loc != position:
    if loc[0] > 1:
        loc[0] -= 1
        loc[1] += 1
    else:
        loc[0] = next_row
        next_row += 1
        loc[1] = 1
    current = next_val(current)

print(current)
