gen_a_factor = 16807
gen_b_factor = 48271

divisor = 2147483647


def generate(a, b):
    """run the generator"""
    while True:
        a = a * gen_a_factor % divisor
        b = b * gen_b_factor % divisor
        yield a & 0xffff == b & 0xffff


def iterate(a, b):
    """run through all of the trials"""
    gen = generate(a, b)

    return sum(next(gen) for _ in range(40000000))


assert iterate(65, 8921) == 588

print(iterate(289, 629))
