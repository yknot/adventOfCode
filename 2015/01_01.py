floors = open('input').read()


# part 1
print 'Ending floor', floors.count('(') - floors.count(')')

# part 2
currentFloor = 0
for i in xrange(len(floors)):
    if currentFloor == -1:
        print 'Basement', i
        break

    if floors[i] == '(':
        currentFloor += 1
    else:
        currentFloor -= 1
        
