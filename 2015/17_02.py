from numpy import vectorize

containers = vectorize(int)(list(open('input')))
count = 0
c = 0
minBins = 21

for i in range(2 ** len(containers)):
    total = 0
    binary = "{0:b}".format(i)[::-1].ljust(20,'0')
    for j in range(len(binary)):
        if int(binary[j]):
            total += containers[j]

    if total == 150 and sum(int(x) for x in binary) <= minBins:
        if sum(int(x) for x in binary) < minBins:
            minBins = sum(int(x) for x in binary)
            count = 0

        count += 1

print count


