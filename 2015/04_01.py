import hashlib

start = 'iwrupvqb'
num = 0

while True:
    m = hashlib.md5()
    m.update(start + str(num))
    if m.hexdigest()[:6] == '000000':
        break

    num += 1

print num
    
