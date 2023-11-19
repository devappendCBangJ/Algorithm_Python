# 30min 소요

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1
    # print(board)

    count = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and visited[r][c] == 0: # 해당 좌표가 방문하지 않은 배추일 때만 방문해야지!!!
                count += 1
                queue = deque([[r, c]])
                while queue:
                    qr, qc = queue.popleft()
                    for i in range(4):
                        nr = qr + dr[i]
                        nc = qc + dc[i]
                        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 and visited[nr][nc] == 0: # 해당 좌표가 방문하지 않은 배추일 때만 방문해야지!!!
                            queue.append([nr, nc])
                            visited[nr][nc] = 1
                # print(visited)
    print(count)