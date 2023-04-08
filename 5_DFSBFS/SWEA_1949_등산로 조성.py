# 라이브러리 불러오기
from copy import deepcopy
from collections import deque

# test case input
T = int(input())

# test case 순회
for test_case in range(1, T + 1):
    # 맵 정보 input 받기
    N, K = list(map(int, input().split()))
    board = []
    
    # 변수 초기화
    max_val = 0
    max_val_coor = []
    max_time_result = 0

    # 맵 생성
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    # 최대값의 좌표 추출 + 해당값 좌표 저장
    max_val = max(list(map(max, board)))
    for y in range(N): # locality 고려
        for x in range(N):
            if board[y][x] == max_val:
                max_val_coor.append([x, y])

    # print(board)
    # print(max_val_coor)

    # 모든 봉우리 고려
    for m_x, m_y in max_val_coor:
        # queue 생성
        queue = deque([])

        # 땅 1개씩 파면서 모든 경우 생각
        for tmp_y in range(N):
            for tmp_x in range(N):
                """
                if y == 2:
                    print(x)
                if m_x == 4 and m_y == 2 and x == 3 and y == 2:
                    print(x, y)
                """
                # tmp_board 생성
                tmp_board = deepcopy(board)

                # 땅 1개씩 파기
                if tmp_x != m_x or tmp_y != m_y:
                    for k in range(K):
                        tmp_board[tmp_y][tmp_x] -= 1

                        # time_board 초기화
                        time_board = [[1 for _ in range(N)] for _ in range(N)]

                        # queue 초기값
                        queue.append([m_x, m_y])

                        # queue 순회
                        while queue:
                            x, y = queue.popleft()
                            
                            # 이웃 순회 (벽 & 나보다 봉우리 큰놈 제외)
                            for n_x, n_y in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                                if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                                    continue
                                elif tmp_board[n_y][n_x] >= tmp_board[y][x]:
                                    continue
                                queue.append([n_x, n_y])
                                time_board[n_y][n_x] = time_board[y][x] + 1
                                if max_time_result < time_board[n_y][n_x]:
                                    max_time_result = time_board[n_y][n_x]
    print(f"#{test_case} {max_time_result}")


# ---------------------------------------------------
# 다른 사람 풀이
# https://chelseashin.tistory.com/2
# ---------------------------------------------------
"""
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        elif chance and A[nr][nc] - K < A[r][c]:
            temp = A[nr][nc]
            A[nr][nc] = A[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance-1)
            visited[nr][nc] = 0
            A[nr][nc] = temp

# main
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = []
    top = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j] > top:
                top = A[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc+1, MAX))
"""
