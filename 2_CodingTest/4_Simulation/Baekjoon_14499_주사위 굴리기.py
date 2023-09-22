from collections import deque

N, M, c, r, K = list(map(int, input().split()))

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dirs = list(map(int, input().split()))
dir_dict = {1:[0, 1], 2:[0, -1], 3:[-1, 0], 4:[1, 0]}

dicey = [0, 0, 0, 0]
dicex = [0, 0]

for k in range(K):
    dir = dirs[k]
    if 0 <= c + dir_dict[dir][1] < M and 0 <= r + dir_dict[dir][0] < N:
        c += dir_dict[dir][1]
        r += dir_dict[dir][0]
        if dir == 1:
            dicey[3], dicex[1], dicey[1], dicex[0] = dicex[1], dicey[1], dicex[0], dicey[3]
        elif dir == 2:
            dicey[3], dicex[0], dicey[1], dicex[1] = dicex[0], dicey[1], dicex[1], dicey[3]
        elif dir == 3:
            dicey[3], dicey[2], dicey[1], dicey[0] = dicey[2], dicey[1], dicey[0], dicey[3]
        elif dir == 4:
            dicey[3], dicey[2], dicey[1], dicey[0] = dicey[0], dicey[3], dicey[2], dicey[1]

        if board[r][c] == 0:
            board[r][c] = dicey[3]
        else:
            dicey[3] = board[r][c]
            board[r][c] = 0
        print(dicey[1])

# ---------------------------------------------------
# 다른 사람 풀이 -> 나와 같은 방식 (근데 왜 내껀 안되지?)
# https://hongcoding.tistory.com/128
# ---------------------------------------------------
"""
n, m, x, y, k = map(int, input().split())

board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = x, y
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
"""