import numpy as np

input = 33100000
debug = False

def get_divisors(n):
    divisors = []
    for i in range(1, int(np.sqrt(n))+1):
        # if it is a divisor
        if n % i == 0:
            # if they are both equal
            if i != n//i:
                # if that elf has delivered less than or equal to 50
                if i <= 50:
                    divisors.append(n//i)
            # if that elf has delivered less than or equal to 50                    
            if n // i <= 50:
                divisors.append(i)

    return divisors
    
    # inefficient
    # return [i for i in range(1, n+1) if n % i == 0]
            


house = 1
while not debug or house < 20:
    if house % 10000 == 0:
        print(house)
    if debug:
        print("House {}".format(house))

    divisors = get_divisors(house)
    presents = sum(divisors) * 11

    if debug:
        print("Presents {}\n".format(presents))

    # if at least input presents found then break
    if presents >= input:
        print("Found {} presents at house {}".format(presents, house))
        break
    
    house += 1 
