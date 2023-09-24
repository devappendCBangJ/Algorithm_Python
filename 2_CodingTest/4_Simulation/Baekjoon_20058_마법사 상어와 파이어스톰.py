# 120min 소요

from collections import deque

N, Q = list(map(int, input().split()))

board = []
board_len = 2 ** N
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for _ in range(board_len):
    board.append(list(map(int, input().split())))
temp_board = [[0 for c in range(board_len)] for r in range(board_len)]
level = list(map(int, input().split()))

for l in level:
    grid_len = 2**l
    grid_unit = [i for i in range(0, board_len, grid_len)]
    # print(grid_unit)

    # 보드 회전
    for rgu in grid_unit:
        for cgu in grid_unit:
            for rgl in range(grid_len):
                for cgl in range(grid_len):
                    temp_board[rgu+cgl][cgu+(grid_len-1)-rgl] = board[rgu+rgl][cgu+cgl] # base좌표계와 Grid 안의 상대 좌표계 헷갈림 주의!!!
    # print(board)
    # print(temp_board)

    # 얼음 녹이기 연산
    minus_board = [[0 for c in range(board_len)] for r in range(board_len)]
    for r in range(board_len):
        for c in range(board_len):
            ice_count = 0
            for dir in range(4):
                nr, nc = r + dr[dir], c + dc[dir]
                if 0 <= nr <= board_len-1 and 0 <= nc <= board_len-1 and temp_board[nr][nc] != 0: # 녹이기 기준 주의!!!
                    ice_count += 1
            if ice_count < 3:
                minus_board[r][c] -= 1 # [r, c]를 append하는 방식으로 저장하는 것이 더 효율적임!!!

    # 실제 얼음 녹이기
    for r in range(board_len):
        for c in range(board_len):
            if minus_board[r][c] == -1 and 1 <= temp_board[r][c]: # temp_board가 0 이하인 경우, -로 바뀌어버림!!!
                board[r][c] = temp_board[r][c] - 1
            else:
                board[r][c] = temp_board[r][c]
# print(board)

# 큰 덩어리 구하기
max_ice = 0
visited_board = [[0 for c in range(board_len)] for r in range(board_len)]
for r in range(board_len):
    for c in range(board_len):
        # print("0 : ", r, c)
        if visited_board[r][c] == 0 and 0 < board[r][c]:
            temp_ice = 0
            queue = deque([[r, c]])
            while queue:
                qr, qc = queue.popleft()
                for dir in range(4):
                    nr, nc = qr + dr[dir], qc + dc[dir] # r, c가 아니라 queue에서 뽑아낸 qr, qc를 써야함 주의!!!
                    # print("1 : ", nr, nc, temp_ice)
                    if 0 <= nr <= board_len-1 and 0 <= nc <= board_len-1 and 0 < board[nr][nc] and visited_board[nr][nc] == 0:
                        temp_ice += 1
                        # print("2 : ", nr, nc, temp_ice)
                        max_ice = max(max_ice, temp_ice)
                        visited_board[nr][nc] += 1
                        queue.append([nr, nc])

# 결과 연산
sum_ice = 0
for line in board:
    sum_ice += sum(line)
print(sum_ice)
print(max_ice)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 거의 완전히 똑같음
# https://kimjingo.tistory.com/131
# ---------------------------------------------------
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def rotate_and_melting(board, len_board, L):
    # Level에 맞게 회전 후 얼음을 녹임
    # :param board: 보드
    # :param len_board: 보드 길이
    # :param L: level
    # :return:
    new_board = [[0] * len_board for _ in range(len_board)] # 회전한 Board 저장 용

    # rotate
    r_size = 2 ** L # 격자 사이즈
    for y in range(0, len_board, r_size): # 격자 시작 좌표 y축
        for x in range(0, len_board, r_size): # 격자 시작 좌표 x축
            for i in range(r_size): # 열 인덱스
                for j in range(r_size): # 행 인덱스
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

    board = new_board
    melting_list = [] # 녹을 얼음 좌표
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))

    # 저장된 얼음들을 녹임
    for y, x in melting_list:
        board[y][x] -= 1

    return board

def check_ice_bfs(board, len_board):
    # 얼음 상태 확인
    # :param board: 보드
    # :param len_board: 보드 가로 길이
    # :return:
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx] # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count) # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)


def solve():
    N, Q = map(int, input().split(' '))
    len_board = 2 ** N
    board = [list(map(int, input().split(' '))) for _ in range(len_board)]
    L_list = list(map(int, input().split(' ')))

    for L in L_list:
        board = rotate_and_melting(board, len_board, L)

    check_ice_bfs(board, len_board)

solve()
"""