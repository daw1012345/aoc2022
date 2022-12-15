def man_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def parse_in():
    with open("day15/input.txt") as f:
        data = []
        raw = f.read().replace(',','').replace(':', '').splitlines()
        for l in raw:
            comps = l.split(' ')
            data.append((int(comps[2][2:]), int(comps[3][2:]), int(comps[8][2:]), int(comps[9][2:])))
    return data


def is_possible(x,y,grid):
    for xs,ys,dist in grid:
        if man_dist(x,y,xs,ys) <= dist:
            return False
    return True

def get_edges(x,y,dist):
    edges = set()
    for dxy in range(0, dist+2):
        edge_dist = dist+1
        edges.add((x+dxy,y+(edge_dist-dxy)))
        edges.add((x+dxy,y-(edge_dist-dxy)))
        edges.add((x-dxy,y+(edge_dist-dxy)))
        edges.add((x-dxy,y-(edge_dist-dxy)))
    return edges


def get_max_x_deflection(y, dist, row_y):
    if y + dist < row_y or y - dist > row_y:
        return -1
    return dist-abs(row_y-y)

def get_taken_in_row(max_deflection, x, y_row):
    taken = set()
    if max_deflection == -1:
        return taken
    
    for i in range(max_deflection+1):
        taken.add((x+i, y_row))
        taken.add((x-i, y_row))
    return taken
    


# P1
ROW = 2000000
grid = parse_in()
everything = set()
for entry in grid:
    dist = man_dist(*entry)
    deflect = get_max_x_deflection(entry[1], dist, ROW)
    everything.update(get_taken_in_row(deflect, entry[0], ROW))

beacons = set(map(lambda x: (x[2],x[3]), grid))

print(len(everything-beacons))
# P2

grid = parse_in()
grid = list(sorted(map(lambda x: (x[0], x[1], man_dist(*x)), grid), key=lambda x: x[2]))
ret = None
for i, thing in enumerate(grid):
    edges = get_edges(*thing)
    for ex, ey in edges:
        if 0 <= ex <= 4000000 and 0 <= ey <= 4000000 and is_possible(ex,ey,grid):
            ret = 4000000*ex+ey
            break
    if ret is not None:
        print(ret)
        break

    
            