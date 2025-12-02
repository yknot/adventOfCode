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
        for val in range(self.first, self.last + 1):
            str_val = str(val)
            if len(str_val) % 2 == 0:
                mid = len(str_val) // 2
                if str_val[:mid] == str_val[mid:]:
                    invalids.append(val)

        return invalids

    def find_all_repeats(self) -> list[int]:
        invalids = []
        for val in range(self.first, self.last + 1):
            str_val = str(val)
            len_val = len(str_val)

            rep_len = 1
            # while we can have at least one repeat
            while rep_len * 2 <= len_val:
                if len_val % rep_len == 0:
                    if str_val[:rep_len] * (len_val // rep_len) == str_val:
                        invalids.append(val)
                        break

                rep_len += 1

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
