
def captcha(digits):
    """calc sum of string if next value matches current value"""
    sum = 0
    half = int(len(digits) / 2)
    for i, d in enumerate(digits):
        # if we are done
        if i == half:
            break
        # if match halfway through then add both
        if digits[i + half] == d:
            sum += int(d) * 2

    return sum


# test cases
assert captcha('1212') == 6
assert captcha('1221') == 0
assert captcha('123425') == 4
assert captcha('123123') == 12
assert captcha('12131415') == 4
# final input
print(captcha(open('input').read().strip()))
