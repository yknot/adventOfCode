from dataclasses import dataclass

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


@dataclass
class Inventory:
    fresh_ranges: list[tuple[int, int]]
    ingredients: list[int]

    def find_fresh_count(self) -> int:
        fresh_ing = 0
        rng_iter = 0
        ing_iter = 0

        while self.ingredients[ing_iter] < self.fresh_ranges[rng_iter][0]:
            ing_iter += 1

        while ing_iter < len(self.ingredients) and rng_iter < len(self.fresh_ranges):
            # if fresh ingredient
            if (
                self.fresh_ranges[rng_iter][0]
                <= self.ingredients[ing_iter]
                <= self.fresh_ranges[rng_iter][1]
            ):
                fresh_ing += 1
                ing_iter += 1
                continue

            # out of range so move to the next
            if self.ingredients[ing_iter] > self.fresh_ranges[rng_iter][1]:
                rng_iter += 1
                continue

            # didn't find a range for this ingredient so move to the next
            if self.ingredients[ing_iter] < self.fresh_ranges[rng_iter][0]:
                ing_iter += 1
                continue

        return fresh_ing

    def find_all_fresh(self) -> int:
        final_pairs = []
        iter = 1

        curr_low, curr_high = self.fresh_ranges[0]

        while iter < len(self.fresh_ranges):
            iter_low, iter_high = self.fresh_ranges[iter]
            # if we can extend the current range
            if curr_high >= iter_low:
                # ensure we take the higher of the two endpoints
                curr_high = max(iter_high, curr_high)
                iter += 1

            else:
                final_pairs.append((curr_low, curr_high))
                curr_low, curr_high = iter_low, iter_high
                iter += 1

        final_pairs.append((curr_low, curr_high))

        total = 0
        for low, high in final_pairs:
            total += high - low + 1

        return total


def parse(inpt: str) -> Inventory:
    rang_raw, ing_raw = inpt.split("\n\n")

    ranges = sorted(
        [tuple(map(int, row.split("-"))) for row in rang_raw.split()],
        key=lambda x: x[0],
    )

    ingredients = sorted([int(ing) for ing in ing_raw.split()])

    return Inventory(ranges, ingredients)


def find_fresh_ingredients_count(inpt: str) -> int:
    inventory = parse(inpt)

    return inventory.find_fresh_count()


def find_all_possible_fresh(inpt: str) -> int:
    inventory = parse(inpt)

    return inventory.find_all_fresh()


with open("05_input") as f:
    data = f.read()

assert find_fresh_ingredients_count(example) == 3
assert find_fresh_ingredients_count(data) == 661

assert find_all_possible_fresh(example) == 14
assert find_all_possible_fresh(data) == 359526404143208
