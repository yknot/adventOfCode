"""advent of code 2016 day 4 part 1"""
import hashlib

door_id = 'abbhdwsy'
code = ''
num = 0

while True:
    m = hashlib.md5()
    full_line = door_id + str(num)
    m.update(full_line.encode('utf-8'))
    if m.hexdigest()[:5] == '00000':
        code += str(m.hexdigest()[5])
        if len(code) == 8:
            break

    num += 1

print(code)
