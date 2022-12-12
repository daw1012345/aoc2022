grid = []
unvisited = set()
start = None
end = None
distances = dict()
prev = dict()

def parse():
    global start, grid, end
    for i, l in enumerate(open('day10/input.txt', 'r').readlines()):
        grid.append(list(l.strip()))
        if 'S' in grid[i]:
            start = (grid[i].index('S'),i)
        if 'E' in grid[i]:
            end = (grid[i].index('E'),i)
        unvisited.update([(x, i) for x in range(len(grid[i]))])
    for n in unvisited:
        distances[n] = len(unvisited) + 1
    distances[end] = 0

parse()

def get_neigh(coord):
    global unvisited
    possible = [(1, 0), (-1, 0), (0, 1), (0,-1)]
    conv = {'E': 'z', 'S':'a'}
    neigh = set()
    for x,y in possible:
        n_c = (coord[0]-x, coord[1]-y)
        if n_c not in unvisited:
            continue
        current = grid[coord[1]][coord[0]]
        n = grid[n_c[1]][n_c[0]] 
        current = conv[current] if current in conv.keys() else current
        n = conv[n] if n in conv.keys() else n
        if ord(current) > ord(n) + 1: # at most 1 higher
            continue
        neigh.add(n_c)
    return neigh

while len(unvisited) > 0:
    u = sorted(list(unvisited), key=lambda x:distances[x])[0]
    unvisited.remove(u)
    for n in get_neigh(u):
        if 1+distances[u] < distances[n]:
            distances[n] = min(distances[n], 1+distances[u])
            prev[n] = u

print(distances[start])
min_dist = len(grid)*len(grid[0])
for yi, y in enumerate(grid):
    for xi, x in enumerate(y):
        if x == 'a' or x == 'S':
            min_dist = min(min_dist, distances[(xi, yi)])
print(min_dist)