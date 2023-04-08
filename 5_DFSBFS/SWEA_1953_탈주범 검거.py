# 라이브러리 불러오기
from collections import deque

# 변수 초기화
case_count = 1
dir_list = {"1": [[-1, 0], [1, 0], [0, 1], [0, -1]], "2": [[0, 1], [0, -1]], "3": [[-1, 0], [1, 0]],
            "4": [[0, -1], [1, 0]], "5": [[1, 0], [0, 1]], "6": [[-1, 0], [0, 1]], "7": [[-1, 0], [0, -1]]}

# 반복 횟수 input
case_all = int(input())

# BFS 함수 정의
def bfs(N, M, C, R, time_board, real_board, result):
    # 방문할 공간 불러오기
    queue = deque([[C, R]])

    # queue 순회
    while queue:
        # 가장 오래된 공간 빼기
        x, y = queue.popleft()

        # 시간 초과할 예정일 시, 종료
        if time_board[y][x] >= L:
            return result

        # 이웃 방문
        for n_x, n_y in dir_list[str(real_board[y][x])]:
            # 벽 건너뛰기
            if y+n_y < 0 or y+n_y >= N or x+n_x < 0 or x+n_x >= M:
                continue
            # 이미 방문한 곳 건너뛰기
            elif time_board[y+n_y][x+n_x] != 0:
                continue
            # 구조가 아무것도 없는 경우 건너뛰기
            elif real_board[y+n_y][x+n_x] == 0:
                continue
            # 이웃과 이어져 있는 방문 queue 등록
            for c_x, c_y in dir_list[str(real_board[y+n_y][x+n_x])]:
                if (n_x+c_x == 0 and n_y+c_y == 0): # 경우 주의!!!
                    queue.append([x+n_x, y+n_y])
                    # time 업데이트 + result 개수 업데이트
                    time_board[y+n_y][x+n_x] = time_board[y][x] + 1
                    result += 1
                    break
    return result

# 케이스 반복
for case_count in range(1, case_all + 1):
    # 초기값 input
    N, M, R, C, L = list(map(int, input().split()))

    # 경기장 선언
    real_board = []
    # 경기장 input
    for _ in range(N):
        real_board.append(list(map(int, input().split()))) # map은 반드시 list로 묶어야한다!!!

    # 변수 초기화
    result = 1
    time_board = [[0 for _ in range(M)] for _ in range(N)]
    time_board[R][C] = 1

    # BFS 순회
    print(f"#{case_count} {bfs(N, M, C, R, time_board, real_board, result)}")
