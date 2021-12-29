"""
Day 16, part 2
"""
from utils import read_input
from math import prod


ops = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def get_header(pkt):
    version = int(pkt[:3], 2)
    ptype = int(pkt[3:6], 2)
    return version, ptype


def parse_literal(pkt):
    literal = ""
    start = 0
    while True:
        literal += pkt[start + 1 : start + 5]
        if pkt[start] == "0":
            return int(literal, 2), pkt[start + 5 :]
        start += 5


def get_length(pkt):
    length_type = pkt[0]
    pkt = pkt[1:]
    if length_type == "0":
        length = int(pkt[:15], 2)
        pkt = pkt[15:]
    elif length_type == "1":
        length = int(pkt[:11], 2)
        pkt = pkt[11:]

    return length_type, length, pkt


def gather_subs(pkt, length_type, length):
    subs = []
    if length_type == "1":
        while len(subs) < length and pkt and int(pkt, 2):
            sub, pkt = parse_packet(pkt)
            subs.append(sub)
    elif length_type == "0":
        num_digits = 0
        while num_digits < length and pkt and int(pkt, 2):
            before = len(pkt)
            sub, pkt = parse_packet(pkt)
            num_digits += before - len(pkt)
            subs.append(sub)

    return subs, pkt


def parse_packet(pkt):
    version, ptype = get_header(pkt)

    if ptype == 4:
        result, pkt = parse_literal(pkt[6:])
    else:
        length_type, length, pkt = get_length(pkt[6:])
        subs, pkt = gather_subs(pkt, length_type, length)
        result = ops[ptype](subs)

    return result, pkt


def get_results(packet):
    bin_packet = bin(int(packet, 16))[2:].zfill(len(packet) * 4)

    result, _ = parse_packet(bin_packet)
    return result


test_inpt = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]

test_out = [3, 54, 7, 9, 1, 0, 0, 1]

for i, t in enumerate(test_inpt):
    assert get_results(t) == test_out[i]


inpt = read_input(16)
try:
    res = get_results(inpt)
    assert res == 258888628940
except:
    print(res)
    raise
