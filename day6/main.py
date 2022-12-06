# Recursive solution
# import sys
# sys.setrecursionlimit(20000)

# def do_puzzle(input, i, range_to_test):
#     return i + range_to_test if len(frozenset(input[:range_to_test])) == range_to_test else do_puzzle(input[1:], i + 1, range_to_test)

# with open("day6/input.txt", 'r') as f:
#     print(do_puzzle(f.readlines()[0], 0, 14))

# Iterative solution
with open("day6/input.txt", 'r') as f:
    a = f.readlines()[0]
    print([len(frozenset(a[x:x+4])) for x in range(len(a)-4)].index(4)+4)
    print([len(frozenset(a[x:x+14])) for x in range(len(a)-14)].index(14)+14)

