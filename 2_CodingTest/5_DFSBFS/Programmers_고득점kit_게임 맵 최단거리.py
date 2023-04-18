# 라이브러리 불러오기
from collections import deque

# 입력 받기
N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# time board 생성
time_board = [[0 for _ in range(M)] for _ in range(N)]
time_board[0][0] = 1

# BFS
def bfs(N, M, board, time_board):
    queue = deque([[0, 0]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            elif board[ny][nx] == 0:
                continue
            elif time_board[ny][nx] != 0:
                continue

            # 목표 지점인 경우
            if nx == M-1 and ny == N-1:
                return time_board[y][x] + 1

            queue.append([nx, ny])
            time_board[ny][nx] = time_board[y][x] + 1

    return -1

print(bfs(N, M, board, time_board))