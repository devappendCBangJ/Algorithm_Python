N, M, K = list(map(int, input().split()))
board = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
for m in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireball.append([r-1, c-1])
    board[r-1][c-1] = [[m, s, d]] # 여러 파이어볼이 합쳐질 때, 여러개가 동시에 있을 수 있으므로 2차원 으로 생성 -> 이러면 split_board를 따로 만들지 않고, move_board만 추가로 만들어줘도 됨!
# print(board)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
odd_even_move_dir = [0, 2, 4, 6]
else_move_dir = [1, 3, 5, 7]
# print(-1 % 4)
for k in range(K):
    # print(fireball)
    move_board = [[[] for _ in range(N)] for _ in range(N)]
    split_board = [[[] for _ in range(N)] for _ in range(N)]
    for r, c in fireball:
        for board_rc in board[r][c]:
            # print(board_rc)
            mr = (r + dy[board_rc[2]] * board_rc[1]) % N # dx, dy <-> column, row 방향 주의! # board의 기존 좌표에 있던 정보를 move_board에 옮겨야함
            mc = (c + dx[board_rc[2]] * board_rc[1]) % N
            # print(board[r][c])
            move_board[mr][mc].append([board_rc[0], board_rc[1], board_rc[2]])
    fireball = []
    # print("moved_board", move_board)
    for r in range(N):
        for c in range(N):
            len_move_fireball = len(move_board[r][c])
            # print(move_board[r][c])
            if len_move_fireball >= 2:
                # print(move_board[r][c])
                total_m, total_s, even_d, odd_d = 0, 0, 0, 1
                is_even, is_odd = True, True
                for m, s, d in move_board[r][c]:
                    total_m += m
                    total_s += s
                    even_d += d
                    odd_d *= d
                    if even_d % 2 == 1:
                        is_even = False
                    if odd_d % 2 == 0:
                        is_odd = False
                m = total_m // 5
                move_board[r][c] = [] # if m == 0 판단보다 위에 있어야함. 그래야 m이 0인 경우도 원소 비워줌!
                if m == 0:
                    continue
                s = total_s // len_move_fireball
                if is_even or is_odd:
                    for d in odd_even_move_dir:
                        split_board[r][c].append([m, s, d])
                else:
                    for d in else_move_dir:
                        split_board[r][c].append([m, s, d])
            if len_move_fireball >= 1:
                fireball.append([r, c])
    for r in range(N):
        for c in range(N):
            board[r][c] = split_board[r][c] + move_board[r][c]

    # print("")
    # for b in board:
    #     print(b)
    # print("")
    # for m in move_board:
    #     print(m)
    # print("")
    # for s in split_board:
    #     print(s)

mass_count = 0
for r, c in fireball:
    for board_rc in board[r][c]:
        mass_count += board_rc[0]
print(mass_count)