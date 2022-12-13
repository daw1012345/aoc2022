from enum import Enum
from functools import cmp_to_key
import itertools

class State(Enum):
    RIGHT = 0
    WRONG = 1
    CONTINUE = 2

def parse():
    packets = []
    with open('day13/input.txt', 'r') as f:
        raw_data = f.readlines()
    
    packet = []
    for l in raw_data:
        if l == '\n':
            packets.append(packet)
            packet = []
        else:
            p, _ = parse_list(l[1:].strip())
            packet.append(p)
    packets.append(packet)
    return packets


def greedy_int_parser(data):
    i = 0
    num = ''
    while data[i].isnumeric():
        num += data[i]
        i += 1
    return int(num),i


def parse_list(data):
    parsed_packet = []
    i = 0
    while i < len(data):
        match data[i]:
            case ' ': pass
            case ',': pass
            case '[': 
                l, parsed_n = parse_list(data[i+1:])
                parsed_packet.append(l)
                i += parsed_n + 1
            case ']': break
            case _:
                num, parsed_n = greedy_int_parser(data[i:])
                parsed_packet.append(num)
                i += parsed_n - 1
        i += 1
    return parsed_packet, i

parsed_data = parse()

def compare_packet(l_list, r_list) -> State:
    ret = State.CONTINUE
    for l, r in zip(l_list, r_list):
        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                ret = State.WRONG
            elif l < r:
                ret = State.RIGHT
        if isinstance(l, list) and isinstance(r, list):
            ret = compare_packet(l, r)
        if isinstance(l, list) and isinstance(r, int):
            ret = compare_packet(l, [r])
        if isinstance(l, int) and isinstance(r, list):
            ret = compare_packet([l], r)

        if ret != State.CONTINUE:
            break
    
    if ret == State.CONTINUE:
        if len(r_list) < len(l_list):
            ret = State.WRONG
        elif len(r_list) > len(l_list):
            ret = State.RIGHT

    return ret

def comparator_packets(x, y):
    result = compare_packet(x,y)
    if result == State.RIGHT:
        return -1
    else:
        return 1

c = 0
for i, (l, r) in enumerate(parsed_data):
    if compare_packet(l, r) == State.RIGHT:
        c += i + 1
print(c)

parsed_data = list(itertools.chain(*parsed_data))

parsed_data.append([[2]])
parsed_data.append([[6]])

srtd = list(sorted(parsed_data, key=cmp_to_key(comparator_packets)))
print((srtd.index([[2]])+1)*(srtd.index([[6]])+1))