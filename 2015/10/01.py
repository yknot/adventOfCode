current = '3113322113'


for _ in range(40):
    next = ''
    loc = 0
    while loc < len(current):
        char = current[loc]
        count = 0
        while loc < len(current) and current[loc] == char:
            count += 1
            loc += 1

        next += str(count) + char


    current = next


print len(current)
