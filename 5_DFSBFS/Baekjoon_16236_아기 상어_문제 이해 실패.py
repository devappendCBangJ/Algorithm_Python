# 라이브러리 불러오기
from collections import deque
from copy import deepcopy

# 맵 크기
N = int(input())
real_board = []
path_board = []

# 변수 정의
time = 0
exp = 0

shark_x, shark_y = 0, 0
shark_size = 2

# 맵 정보
for line in range(N):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        shark_x, shark_y = tmp.index(9), line
    real_board.append(tmp)

# 맵 복사
path_board = deepcopy(real_board)
# print(help(list))
# print(real_board)
# print(path_board)
# print(shark_y, shark_x)

# 엄마 호출 여부 함수 정의
def there_food(path_board, shark_size):
    for line in path_board:
        for unit in line:
            if shark_size - unit > 0:
                return "food"

    # 다차원 리스트에서 numpy 사용하지 않고, 특정한 경우 만족하는 원소가 있는지 확인!!!

# BFS함수 정의
def bfs(path_board, shark_size, shark_x, shark_y, time, exp):
    # 먹을 수 있는 먹이 존재 여부 확인
    if there_food(path_board, shark_size) != "food":
        return time

    # queue 선언
    queue = deque([[shark_x, shark_y]])

    # 지나간 경로 업데이트
    path_board[shark_y][shark_x] = 100  # 이미 방문한 놈은 방문하지 않기 위함

    # 처음 상어가 머문 공간 : 사실은 빈공간!!!
    real_board[shark_y][shark_x] = 0

    # queue 순회
    while queue:
        # print(queue)
        # queue에서 오래된 이웃 좌표 하나씩 빼오기
        shark_x, shark_y = queue.popleft()

        # 이웃 순회
        for n_x, n_y in [[shark_x, shark_y-1], [shark_x-1, shark_y], [shark_x+1, shark_y], [shark_x, shark_y+1]]:
            # 맵 바깥으로 나간 경우 : 가지 않음
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue
            # 상어보다 큰 경우 or 이미 방문한 경우 : 가지 않음
            elif path_board[n_y][n_x] > shark_size:
                continue
            # 상어보다 작은 경우 : 먹어 + time 업데이트 + 경험치 업데이트 + 새로운 탐험 시작
            elif 0 < path_board[n_y][n_x] < shark_size:
                # 먹어
                real_board[n_y][n_x] = 0

                # time 업데이트
                time = path_board[shark_y][shark_x] + 1 - 100

                # 맵 복사!!!
                path_board = deepcopy(real_board)
                path_board[n_y][n_x] = time + 100

                # 경험치 업데이트
                exp += 1

                # 새로운 탐험 시작
                shark_x, shark_y = n_x, n_y
                queue = deque([[shark_x, shark_y]])

                # size 증가 여부 확인 -> 증가!!!
                if exp == shark_size:
                    shark_size += 1
                    exp = 0

                # 먹을 수 있는 먹이 존재 여부 확인!!!
                if there_food(path_board, shark_size) != "food":
                    return time

                # print("존재", path_board)

                # 같은 거리의 경로가 중복해서 추가되는 것을 막기 위해 break!!!
                break
            # 상어와 같은 크기인 경우 or 빈 공간인 경우 : 지속적으로 탐험
            else:
                path_board[n_y][n_x] = path_board[shark_y][shark_x] + 1
                # print("빔", path_board)
                queue.append([n_x, n_y])

    return time

# BFS 동작
time = bfs(path_board, shark_size, shark_x, shark_y, time, exp)

# 결과 출력
print(time)