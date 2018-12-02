# read input
nums = [int(i) for i in open('01_input')]

seen = set()
tot = 0
found = False

# keep going once at the end of nums
while 1:
    # loop
    for i in nums:
        tot += i
        # if dup freq
        if tot in seen:
            print(tot)
            found = True
            break

        # add unseen
        seen.add(tot)

    if found:
        break
