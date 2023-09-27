# ---------------------------------------------------
# 그래프 시간복잡도 개선 전략 : 2D Graph -> 1D Graph
# https://taemham.github.io/posts/Algo_2Dgraph/
# ---------------------------------------------------

# 문제 가정 : 행 크기 R, 열 크기 C인 그래프에서, (0, 0)부터 시작해서 BFS로 모든 칸 탐색 + 방문 time step에 맞게 순서 붙임

import time
from collections import deque

R, C = 10, 10

# 2차원 BFS
board = [[0 for _ in range(R)] for _ in range(C)]
visited_board = [[0 for _ in range(R)] for _ in range(C)]
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
queue = deque([[0, 0, 0]])

start = time.time()

visited_board[0][0] = 1
board[0][0] = 1
while queue: # queue를 deque말고 list로 선언한 채로, while로 popleft하지 않고 for으로 queue 돌리면, BFS가 끝나도 queue를 기억할 수 있음!!!
    r, c, step = queue.popleft()
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr <= R-1 and 0 <= nc <= C-1 and not visited_board[nr][nc]:
            visited_board[nr][nc] = 1
            queue.append([nr, nc, step+1])
            board[nr][nc] = step+1

end = time.time()
print(f"2D time : {end-start}")
print(*board, sep='\n')

# 1차원 BFS
L = C + 1
board = [0] * R * L # 열의 개수 : L, 행의 개수 : R -> 열 방향의 마진 추가를 통해, 행이 바뀌는 지점에서 인접한 원소라고 판단하는 것 방지!!!
visited_board = [0] * R * L + [1] * L # 열의 개수 : L, 행의 개수 : L -> 열 방향, 행 방향 마진 추가를 통해, 격자 밖으로 벗어나는 것 방지. visited_board[-1]처럼 원소 인덱스가 -가 되더라도, 이미 열방향의 마진을 추가해둬서 문제 없음!!!
visited_board[C:R*L:L] = [1] * R
drc = [1, -1, L, -L] # 열의 개수 : L -> 바로 아래 or 위칸으로 이동하려면 +-L!!!
queue = deque([[0, 0]])

start = time.time()

visited_board[0] = 1
board[0] = 1
while queue:
    rc, step = queue.popleft()
    for dir in drc:
        nrc = rc + dir
        if not visited_board[nrc]:
            visited_board[nrc] = 1
            queue.append([nrc, step+1])
            board[nrc] = step+1

end = time.time()
print(f"1D time : {end-start}")
for r in range(0, R*L, L):
    print(board[r:r+C])