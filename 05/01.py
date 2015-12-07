
import re
words = open('input').readlines()

words = [w.strip() for w in words]

vowels = 'aeiou'
bad = ['ab', 'cd', 'pq', 'xy']

final = []
# check for vowels
for w in words:
    count = 0
    for v in vowels:
        count += w.count(v)

    prev = ''
    found = 0
    for l in w:
        if l == prev:
            found = 1
            break
        prev = l

    foundBad = 0
    for b in bad:
        if w.find(b) >= 0:
            foundBad = 1
            break

    if count >= 3 and found and not foundBad:
        final.append(w)



print len(final)
    
        
        
    
## part 2

final = []
p = re.compile(ur'(.).\1')
r = re.compile(ur'(..).*\1')
for w in words:
    check1 = 0
    check2 = 0
    if len(re.findall(r, w)) > 0:
        check1 = 1

    if len(re.findall(p, w)) > 0:
        check2 = 1

    if check1 and check2:
        final.append(w)


print len(final)
 

        
