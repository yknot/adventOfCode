"""Day 4 Part 2"""
from collections import defaultdict


class Guard:
    """Guard class"""

    def __init__(self, gid):
        self.gid = gid
        self.total = 0
        self.asleep = defaultdict(int)

    def add_time(self, s, e):
        """add sleep time"""
        self.total += e - s
        for i in range(s, e):
            self.asleep[i] += 1


def parse_input(inpt):
    """parse input"""
    guards = {}
    i = 0
    while i < len(inpt):

        assert "Guard" in inpt[i]
        gid = int(inpt[i].split()[3][1:])
        if gid not in guards:
            guards[gid] = Guard(gid)

        i += 1
        while "Guard" not in inpt[i]:
            assert "asleep" in inpt[i]
            start_time = int(inpt[i][15:17])

            i += 1
            assert "wake" in inpt[i]
            end_time = int(inpt[i][15:17])

            guards[gid].add_time(start_time, end_time)
            i += 1
            if i == len(inpt):
                break
    return guards


def solve(inpt):
    """driver function"""
    guards = parse_input(inpt)

    max_count = 0
    max_gid = 0
    max_minute = 0
    for gid, g in guards.items():
        if not g.asleep:
            continue
        minute = max(g.asleep, key=g.asleep.get)
        if g.asleep[minute] > max_count:
            max_count = g.asleep[minute]
            max_gid = gid
            max_minute = minute

    return max_gid * max_minute


if __name__ == "__main__":
    test = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

    assert solve(test.split("\n")) == 4455
    assert solve(sorted(open("04_input").readlines())) == 65854
