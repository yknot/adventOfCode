import re


def nextLetter(c):
    if c != 'z':
        return chr(ord(c) + 1)
    else:
        return 'a'


def nextString(string, loc, norm = True):
    if norm:
        return string[:loc] + nextLetter(old[loc]) + string[loc+1:]

    loc += 1
    while loc < len(string)-1:
        string = string[:loc] + 'z' + string[loc+1:]
        loc += 1
    return string

def checkSequence(string):
    i = 0
    while i < len(string) - 2:
        first = ord(string[i])
        second = ord(string[i+1])
        third = ord(string[i+2])
        if third - second == 1 and second - first == 1:
            return True
        i+=1

    return False

# test input
# old = 'ay'
# old = 'abcdefgh'   # answer = abcdffaa
# old = 'ghijklmn'  # answer = ghjaabcc

# real input
old = 'vzbxkghb'

rep = re.compile(ur'.*(.)\1.*(.)\2.*')

while True:
    # first increment the string
    loc = len(old) - 1
    while loc >= 0:
        if old[loc] != 'z':
            old = nextString(old, loc)
            break
        else:
            old = nextString(old, loc)
            loc-=1

    # second check validity
    # check for i, o, l
    if old.find('i') >= 0:
        old = nextString(old, old.find('i'), False)
        continue

    if old.find('o') >= 0:
        old = nextString(old, old.find('o'), False)
        continue

    if old.find('l') >= 0:
        old = nextString(old, old.find('l'), False)
        continue

    # check for sequence
    if not checkSequence(old):
        continue

    # check for repeats
    if len(re.findall(rep, old)) == 0:
        continue


    break




print old
