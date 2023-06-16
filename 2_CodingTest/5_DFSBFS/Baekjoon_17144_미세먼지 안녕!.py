# 90분 소요

# 입력
R, C, T = list(map(int, input().split()))

board = []
for r in range(R):
    board.append(list(map(int, input().split())))
    if board[r][0] == -1:
        machine_row = r
# print(board)
# print(machine_row)

# t초 순회
for _ in range(T):
    # 확산
    spread_board = [[0 for _ in range(C)] for _ in range(R)] # for문 돌때마다 초기화 시켜주지 않으면 이전 시간에서의 spread값이 남아있음
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                spread = board[r][c] // 5
                for nr, nc in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
                    if nr >= 0 and nr < R and nc >= 0 and nc < C and (board[nr][nc] != -1):
                        spread_board[r][c] -= spread
                        spread_board[nr][nc] += spread
    for r in range(R):
        for c in range(C):
            board[r][c] += spread_board[r][c]
    # print("1", board)

    # 공기 청정
    up_dir = [[-1, 0, 0, 0], [0, 1, 0, C-1], [1, 0, machine_row-1, C-1], [0, -1, machine_row-1, 0]]
    down_dir = [[1, 0, R-1, 0], [0, 1, R-1, C-1], [-1, 0, machine_row, C-1], [0, -1, machine_row, 0]]
    machine_coor_dir = [[(machine_row-1)-1, 0, up_dir], [machine_row+1, 0, down_dir]]

    for i, (r, c, dir) in enumerate(machine_coor_dir):
        if i == 0:
            board[(machine_row-1)-1][0] = 0
        else:
            board[machine_row+1][0] = 0
        for dir_r, dir_c, last_r, last_c in dir:
            while r != last_r or c != last_c: # and로 하면 둘 중에 하나라도 만족하면 while문 빠져나와버림. 둘 다 만족해야 빠져나오게 하려면 or 조건을 써줘야함. and를 쓸거면 수식 2개를 묶어줘야함
                tmp_r, tmp_c = r + dir_r, c + dir_c
                board[r][c] = board[tmp_r][tmp_c]
                r, c = tmp_r, tmp_c
                # print(r, c)
                # print("2", board)
    # print(board[machine_row-1][1])
    board[machine_row-1][1] = 0
    # print(board[machine_row - 1][1])
    board[machine_row][1] = 0
    # print("3", board)

print(sum([sum(b) for b in board])+2)