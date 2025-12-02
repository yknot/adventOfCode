from dataclasses import dataclass

example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


@dataclass
class ID:
    first: int
    last: int

    def find_invalid_ids(self, strict: bool = False) -> list[int]:
        if strict:
            res = self.find_all_repeats()
        else:
            res = self.find_double_repeats()
        return res

    def find_double_repeats(self) -> list[int]:
        invalids = []

        min_double = max(len(str(self.first)) // 2, 1)
        max_double = len(str(self.last)) // 2
        for half in range(10 ** (min_double - 1), 10**max_double):
            str_half = str(half)
            val = int(str_half + str_half)
            if self.first <= val <= self.last:
                invalids.append(val)

        return invalids

    def find_all_repeats(self) -> list[int]:
        invalids = []

        min_length = max(len(str(self.first)), 2)
        max_length = len(str(self.last)) + 1

        # generate all lengths of numbers that could be in the range
        for num_digits in range(min_length, max_length):
            # for all the lengths of repeated patterns
            for rep_len in range(1, num_digits // 2 + 1):
                if num_digits % rep_len != 0:
                    continue
                reps = num_digits // rep_len

                for rep in range(10 ** (rep_len - 1), 10**rep_len):
                    val = int(str(rep) * reps)
                    if self.first <= val <= self.last and val not in invalids:
                        invalids.append(val)

        return invalids


def parse(inpt: str) -> list[ID]:
    ids = []

    for pair in inpt.split(","):
        first, last = pair.split("-")

        ids.append(ID(int(first), int(last)))

    return ids


def sum_invalid_ids(inpt: str, strict: bool = False) -> int:
    ids = parse(inpt)
    total = 0
    for id in ids:
        invalids = id.find_invalid_ids(strict)
        total += sum(invalids)

    return total


with open("02_input") as f:
    data = f.read()

assert sum_invalid_ids(example) == 1227775554
assert sum_invalid_ids(data) == 54641809925

assert sum_invalid_ids(example, strict=True) == 4174379265
assert sum_invalid_ids(data, strict=True) == 73694270688
