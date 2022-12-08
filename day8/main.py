data = list(map(lambda x: [-1] + list(map(lambda s: int(s), x.strip())) + [-1], open("day8/input.txt", 'r').readlines()))
data.insert(0, len(data[0])*[-1])
data.append(len(data[0])*[-1])
data_inverse = list(map(list, zip(*data)))
res_1 = dict()
res_2 = dict()

for x in range(1, len(data[0])-1):
    for y in range(1, len(data)-1):
        sides = [list(reversed(data[y][:x])),data[y][x+1:],list(reversed(data_inverse[x][:y])),data_inverse[x][y+1:]]
        if True in list(map(lambda s: max(s) < int(data[y][x]), sides)):
            res_1[(x-1,y-1)] = True

        a = 1
        for side in sides:
            i = 0
            if side == [-1]:
                continue
            while i < len(side) and side[i] < data[y][x] and side[i] != -1:
                i += 1
            if i != len(side) - 1:
                i += 1
            a *= i
        res_2[(x-1,y-1)] = a

print(len(res_1.values()))
print(max(res_2.values()))