n, m = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(n)]
commands = input()


def is_valid(r, c):
    return r >= 0 and c >= 0 and r < n and c < m


def mutate_bunnies(matrix):
    global is_dead
    to_change = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'B':
                for d in dirs:
                    r, c = dirs[d][0] + i, dirs[d][1] + j
                    if is_valid(r, c):
                        if (r,c) not in to_change and matrix[r][c] != 'B':
                            to_change.append((r, c))

    for ch in to_change:
        if matrix[ch[0]][ch[1]] == 'P':
            is_dead = True
        matrix[ch[0]][ch[1]] = 'B'

    return matrix



dirs = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1],
}

row, col = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'P':
            row, col = i, j

is_dead = False
is_won = False
coordinates = []
for command in commands:
    if is_won:
        break
    if is_dead:
        break
    rtg = dirs[command][0] + row
    ctg = dirs[command][1] + col
    matrix[row][col] = '.'

    if is_valid(rtg, ctg):
        to_move = matrix[rtg][ctg]
        coordinates = [rtg, ctg]

        if to_move == 'B':
            is_dead = True

        elif to_move == '.':
            #matrix[row][col] = '.'
            matrix[rtg][ctg] = 'P'
        row = rtg
        col = ctg

    else:
        is_won = True
        #matrix[row][col] = '.'
        coordinates = [row, col]

    matrix = mutate_bunnies(matrix)

for row in matrix:
    print(''.join(row))

if is_won:
    print(f'won: {coordinates[0]} {coordinates[1]}')
if is_dead:
    print(f'dead: {coordinates[0]} {coordinates[1]}')


# 5 5
# BBBBB
# BBBBB
# BBBBB
# .BBBB
# P....
# RLLL