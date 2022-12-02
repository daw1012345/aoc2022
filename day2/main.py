from collections import defaultdict
with open("day2/input.txt", 'r') as fd:
    b = fd.readlines()
    print("Part 1: " + str(sum(map(lambda x: (defaultdict(lambda: 0, {"A Y": 6, "B Z": 6,"C X": 6,"A X": 3,"B Y": 3,"C Z": 3})[x.strip()] + ord(x.split(' ')[1].strip())-87), b))))
    print("Part 2: " + str(sum(map(lambda x: (3 * (ord(x.strip().split(' ')[1]) - 88)) + {'X': lambda n: 1 + (ord(n) - 66) % 3, 'Y': lambda n: (ord(n) - 64), 'Z': lambda n: 1+(ord(n) - 64) % 3}[x.strip().split(' ')[1]](x.strip().split(' ')[0]), b))))