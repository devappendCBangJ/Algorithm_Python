from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input())))

houses = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == 0:
            queue = deque([[r, c]])
            visited[r][c] = 1 # 첫 방문 집도 visited를 업데이트 해줘야함!!!
            house_count = 1
            while queue:
                qr, qc = queue.popleft()
                for i in range(4):
                    nr = qr + dr[i]
                    nc = qc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 1 and visited[nr][nc] == 0:
                        queue.append([nr, nc])
                        visited[nr][nc] = 1
                        house_count += 1
            houses.append(house_count)

print(len(houses))
houses.sort()
for house in houses:
    print(house)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 나와 같은 풀이
# https://hongcoding.tistory.com/71
# ---------------------------------------------------
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
"""