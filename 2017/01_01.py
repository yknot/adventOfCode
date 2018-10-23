
def captcha(digits):
    """calc sum of string if next value matches current value"""
    sum = 0
    for i, d in enumerate(digits):
        # if at last one then look at first
        if i == len(digits) - 1:
            if digits[0] == d:
                sum += int(d)
        # if matches next then add
        elif digits[i + 1] == d:
            sum += int(d)

    return sum


# test cases
assert captcha('1122') == 3
assert captcha('1111') == 4
assert captcha('1234') == 0
assert captcha('91212129') == 9
# final input
print(captcha(open('input').read().strip()))
