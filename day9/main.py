STRAIGHT_MOVES = [(0,1),(1,0), (0,-1), (-1,0)]
DIAG_MOVES = [(1,1), (1,-1), (-1,1), (-1,-1)]
SNAKE_LEN = 10

snake, current_tail = (0,0), (0,0)
visited = {(0,0)}
snake = [(0,0) for _ in range(SNAKE_LEN)]

def move_snake():
    for i in range(len(snake)):
        if i == 0: 
            continue
        if snake[i] in [(snake[i-1][0]-xd, snake[i-1][1]-yd) for (xd,yd) in DIAG_MOVES+STRAIGHT_MOVES+[(0,0)]]: 
            continue
        common = sorted(set([(snake[i][0]+xd, snake[i][1]+yd) for (xd,yd) in STRAIGHT_MOVES+DIAG_MOVES]).intersection(set([(snake[i-1][0]+xd, snake[i-1][1]+yd) for (xd,yd) in STRAIGHT_MOVES+DIAG_MOVES])), key=lambda x: x[0]+x[1])
        snake[i] = common.pop()
    visited.add(snake[-1])

for cmd in open("day9/input.txt", 'r').readlines():
    dir = cmd.split(' ')[0]
    n = int(cmd.split(' ')[1])
    for _ in range(n):
        match dir:
            case 'R':
                snake[0] = (snake[0][0] + 1, snake[0][1])
            case 'L':
                snake[0] = (snake[0][0] - 1, snake[0][1])
            case 'U':
                snake[0] = (snake[0][0], snake[0][1]+1)
            case 'D':
                snake[0] = (snake[0][0], snake[0][1]-1)
        move_snake()

print(len(visited))




