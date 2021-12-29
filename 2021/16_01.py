"""
Day 16
"""
from utils import read_input


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


def parse_packet(pkt):
    version, ptype = get_header(pkt)

    if ptype == 4:
        literal, pkt = parse_literal(pkt[6:])
    else:
        length_type, length, pkt = get_length(pkt[6:])
        while int(pkt, 2):
            sub_version, pkt = parse_packet(pkt)
            version += sub_version

    return version, pkt


def get_versions(packet):
    bin_packet = bin(int(packet, 16))[2:].zfill(len(packet) * 4)

    version, _ = parse_packet(bin_packet)
    return version


test_inpt = [
    "D2FE28",
    "38006F45291200",
    "EE00D40C823060",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]

test_out = [6, 9, 14, 16, 12, 23, 31]

for i, t in enumerate(test_inpt):
    assert get_versions(t) == test_out[i]


inpt = read_input(16)
try:
    res = get_versions(inpt)
    assert res == 923
except:
    print(res)
    raise
