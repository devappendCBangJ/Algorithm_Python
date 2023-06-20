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

# ---------------------------------------------------
# 다른 사람 풀이 -> 풀이 방식 같음
# ---------------------------------------------------
"""
from collections import defaultdict

N, M, K = map(int, input().split())
fireballs = defaultdict(list)
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r - 1, c - 1)].append((m, s, d))  # fireballs[(r, c)] : [(m, s, d), (m, s, d)...]

dy8 = (-1, -1, 0, 1, 1, 1, 0, -1)  # 8방향
dx8 = (0, 1, 1, 1, 0, -1, -1, -1)  # 8방향


def move_fireballs():
    # 파이어볼 이동
    global fireballs
    new_fireballs = defaultdict(list)  # 이동 후의 파이어볼 정보
    for loc, info_list in fireballs.items():
        sy, sx = loc
        for m, s, d in info_list:
            ny = (sy + dy8[d] * s) % N  # d방향으로 s만큼 이동 후 N과 나머지 연산을 해줌
            nx = (sx + dx8[d] * s) % N  # d방향으로 s만큼 이동 후 N과 나머지 연산을 해줌
            new_fireballs[(ny, nx)].append((m, s, d))

    fireballs = new_fireballs.copy()


def all_odd_or_even(dirs):
    # 방향이 모두 홀수 혹은 짝수인 경우 True, 아닌 경우 False 반환
    odd_flag, even_flag = False, False
    for d in dirs:
        if d % 2 == 1:
            odd_flag = True  # 홀수 발견
        if d % 2 == 0:
            even_flag = True  # 짝수 발견

    if odd_flag and even_flag:  # 홀/짝 모두 발견된 경우 False 반환
        return False
    return True


def change_duplicate_fireballs():
    # 좌표가 중복된 파이어볼 처리
    global fireballs
    new_fireballs = defaultdict(list)  # 처리후의 파이어볼 정보

    for loc, info_ilst in fireballs.items():
        if len(info_ilst) == 1:  # 해당 좌표에 파이어볼이 1개인 경우
            new_fireballs[loc].append(info_ilst[0])
            continue

        # 파이어볼이 중복된 경우
        sum_m, sum_s, dirs = 0, 0, []  # 질량합, 속도합, 방향리스트
        for m, s, d in info_ilst:
            sum_m += m
            sum_s += s
            dirs.append(d)
        new_m = int(sum_m / 5)  # 새로운 파이어볼 질량
        if new_m == 0:  # 질량이 0인 경우 소멸되므로 continue
            continue
        new_s = int(sum_s / len(info_ilst))  # 새로운 파이어볼 속도
        new_dirs = [0, 2, 4, 6] if all_odd_or_even(dirs) else [1, 3, 5, 7]  # 새로운 파이어볼 방향(all_odd_or_even() 함수의 결과에 따름)
        for new_d in new_dirs:
            new_fireballs[loc].append((new_m, new_s, new_d))

    fireballs = new_fireballs.copy()


for _ in range(K):  # k번 반복
    move_fireballs()
    change_duplicate_fireballs()

result = 0
for loc, info_list in fireballs.items():  # 파이어볼 리스트에서 질량합을 구함
    for m, s, d in info_list:
        result += m
print(result)
"""