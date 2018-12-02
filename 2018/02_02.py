from collections import defaultdict


inpt = [i.strip('\n') for  i in open('02_input')]

# early stopping
found = False
for line in inpt:
    for line2 in inpt:
        # if the same
        if line == line2:
            continue
        # if not the same length
        if len(line) != len(line2):
            continue

        count = 0
        tmp = ''
        for i, l in enumerate(line):
            # early stopping
            if count > 1:
                break
            # construct answer
            if l == line2[i]:
                tmp += l
            else:
                count += 1

        # if answer
        if count == 1:
            print(tmp)
            found = True
            break

    # early stopping
    if found:
        break

        
        
