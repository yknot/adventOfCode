gen_a_factor = 16807
gen_b_factor = 48271
divisor = 2147483647


def generate_a(a):
    """run the generator"""
    while True:
        a = a * gen_a_factor % divisor
        if a % 4 == 0:
            yield a & 0xffff


def generate_b(b):
    """run the generator for b"""
    while True:
        b = b * gen_b_factor % divisor
        if b % 8 == 0:
            yield b & 0xffff


def iterate(a, b):
    """run through all of the trials"""
    gen_a = generate_a(a)
    gen_b = generate_b(b)

    total = 0
    for _ in range(5000000):
        if next(gen_a) == next(gen_b):
            total += 1

    return total


assert iterate(65, 8921) == 309

print(iterate(289, 629))
