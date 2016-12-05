"""advent of code 2016 day 4 part 2"""
import hashlib

door_id = 'abbhdwsy'
code = ['_'] * 8
num = 0

while True:
    m = hashlib.md5()
    full_line = door_id + str(num)
    m.update(full_line.encode('utf-8'))
    hex_val = m.hexdigest()
    if hex_val[:5] == '00000' and not hex_val[5].isalpha():
        idx = int(hex_val[5])
        if idx < 8 and code[idx] == '_':
            code[int(m.hexdigest()[5])] = m.hexdigest()[6]
            if code.count('_') == 0:
                break

    num += 1

print(''.join(code))
