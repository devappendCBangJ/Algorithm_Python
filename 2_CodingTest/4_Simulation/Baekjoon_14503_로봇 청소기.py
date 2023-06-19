N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# print(board)

flag = 0
count = 0
dx = [0, 1, 0, -1] # 반시계 이동 주의!
dy = [-1, 0, 1, 0]

while flag == 0:
    moved = False
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1
    for _ in range(4):
        d = (d - 1) % 4
        if 0 <= r + dy[d] < N and 0 <= c + dx[d] < M and board[r + dy[d]][c + dx[d]] == 0:
            r += dy[d]
            c += dx[d]
            moved = True
            break
    if moved == False:
        if 0 <= r - dy[d] < N and 0 <= c - dx[d] < M and board[r - dy[d]][c - dx[d]] != 1: # 이동할 곳이 쓰레기를 이미 치운 곳이여도 이동 가능! 단, 벽인 경우는 이동 불가능!
            r -= dy[d]
            c -= dx[d]
        else:
            break
    # for b in board:
    #     print(b)
    # print("")
print(count)