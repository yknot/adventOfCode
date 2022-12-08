"""
Day 7
"""
from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int

    def string(self, spacing=""):
        return f"{spacing}- {self.name} (file, size={self.size})\n"


@dataclass
class Directory:
    name: str
    items: list = field(default_factory=list)
    parent = None
    size: int = 0

    def __repr__(self):
        return self.string()

    def string(self, spacing=""):
        res = f"{spacing}- {self.name} (dir, size={self.size})\n"
        for i in self.items:
            res += i.string(spacing=spacing + "  ")
        return res

    def get_sizes(self, prefix="") -> dict:
        sizes = {}
        my_total = 0
        for i in self.items:
            if isinstance(i, File):
                my_total += i.size
            else:
                sizes.update(i.get_sizes(prefix=self.name + "/"))
                my_total += sizes[self.name + "/" + i.name]

        sizes[prefix + self.name] = my_total
        self.size = my_total
        return sizes


def get_folder_size(inpt):
    structure = parse_file_tree(inpt)

    sizes = structure.get_sizes()

    final = sum([v for _, v in sizes.items() if v <= 100000])
    return final


def parse_file_tree(inpt):
    i = 1
    structure = Directory("/")
    pointer = structure
    while i < len(inpt):
        if inpt[i].startswith("$ cd"):
            d = inpt[i].split()[-1]
            # if root
            if d == "/":
                pointer = structure
            # if up one
            elif d == "..":
                pointer = pointer.parent
            else:
                for item in pointer.items:
                    if isinstance(item, Directory) and item.name == d:
                        pointer = item

        elif inpt[i].startswith("$ ls"):
            i += 1
            while i < len(inpt):
                if inpt[i].startswith("$"):
                    break
                elif inpt[i].startswith("dir"):
                    d = Directory(inpt[i].split()[1])
                    d.parent = pointer
                    pointer.items.append(d)
                else:
                    size, name = inpt[i].split()
                    for item in pointer.items:
                        if isinstance(item, File) and item.name == name:
                            item.size = size
                            continue

                    f = File(name, int(size))
                    pointer.items.append(f)

                i += 1

            i -= 1

        i += 1

    return structure


with open("07_test_input") as f:
    test_inpt = f.read().split("\n")

with open("07_input") as f:
    inpt = f.read().split("\n")

assert get_folder_size(test_inpt) == 95437

assert get_folder_size(inpt) == 1743217
