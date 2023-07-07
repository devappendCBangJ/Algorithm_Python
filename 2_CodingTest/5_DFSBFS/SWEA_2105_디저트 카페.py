# ---------------------------------------------------
# 01:09:25
# ---------------------------------------------------
from collections import deque

dc = [1, -1, -1, 1]
dr = [1, 1, -1, -1]

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    max_len = -1
    for row in range(0, N-2):
        for col in range(1, N-1):
            queue = deque([[row, col, set([board[row][col]])]]) # queue단위로 경로 기억! 방향 전환 횟수까지 기억하고, 조건문을 추가했으면, 방향 전환을 위한 for문, queue_len for문을 쓰지 않아도 풀 수 있었네!
            for i in range(4):
                queue_len = len(queue)
                for _ in range(queue_len): # 이전 방향 전환에서, 새로 추가한 경로 개수 만큼만 이동! 이렇게 하지 않으면, queue에 계속 새로 append되면서 '1번의 방향 전환'단위로 연산을 처리할 수 없음!
                    r, c, track = queue.popleft()
                    r, c = r+dr[i], c+dc[i] # 방향 전환 후, 무조건 1번은 전진해야함!
                    while 0 <= r < N and 0 <= c < N and (board[r][c] not in track): # 직사각형 형태로 움직이므로, 초반 2번의 방향 전환을 통해 변의 길이를 알 수 있음. 그래서 변의 길이를 초과하지 않고, 딱 맞아떨어지게 이동할 수 있는데 귀찮아지니까 이렇게 하지 않았음!
                        track = track.copy() # track을 그대로 사용하면 변수의 주소가 복사되므로 copy 사용!
                        track.add(board[r][c])
                        queue.append([r, c, track])
                        r, c = r+dr[i], c+dc[i]
                    if r == row and c == col and max_len < len(track): # 종점 도달 시, 최대값으로 업데이트!
                        max_len = len(track)
    print(f'#{test_case} {max_len}')

# ---------------------------------------------------
# 다른 사람 풀이 -> DFS 풀이
# https://hyunse0.tistory.com/338
# ---------------------------------------------------
"""
import sys
sys.stdin = open('input.txt')

def dfs(x, y, path, way): # 방향 몇 번 전환했는지 기억해둠!
    global cnt, i, j

    if way == 3 and x == i and y == j and len(path) > 2:
        cnt = max(cnt, len(path))
        return

    if 0 <= x < N and 0 <= y < N and cafe[x][y] not in path:
        new_path = path + [cafe[x][y]]

        # 직진
        nx, ny = x + dxy[way][0], y + dxy[way][1] # 방향 전환 후에는 무조건 직진!
        dfs(nx, ny, new_path, way)

        # 꺾는 경우
        if way < 3:
            nx, ny = x + dxy[way + 1][0], y + dxy[way + 1][1]
            dfs(nx, ny, new_path, way + 1)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    cnt = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)

    print('#{} {}'.format(t, cnt))
"""