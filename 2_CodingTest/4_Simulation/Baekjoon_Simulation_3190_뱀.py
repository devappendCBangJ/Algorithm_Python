# 라이브러리 불러오기
from collections import deque

# 맵 크기 불러오기
N = int(input())
board = [[0 for j in range(N)] for i in range(N)] # 다차원 리스트 초기화 하면서 생성!!!

# 사과 위치 불러오기 + 맵에 저장
K = int(input())
for i in range(K):
    tmp = list(map(int, input().split()))
    board[tmp[0]-1][tmp[1]-1] = 1

# 방향 전환 횟수 불러오기 + 방향 회전 시간 + 방향 저장
L = int(input())
time_dir = {}
for i in range(L):
    tmp = input().split()
    time_dir[tmp[0]] = tmp[1] # input 불러오자 마자 할당!!!

# 변수 선언
dir_table = {'0':'21', '1':'12', '2':'01', '3':'10'}
time = 0
x, y = 0, 0
dir = '0'
size = 1
queue = deque([[x, y]])

# 방향 전환
def dir_change(now_dir, change_dir):
    dir = int(now_dir)
    dir = dir + 1 if change_dir == 'D' else dir - 1

    if dir == 4: # if-else 또는, if-elif-else 구조만 1줄 if문 사용 가능
        dir = 0
    elif dir == -1:
        dir = 3
    return str(dir)

while(True):
    # print(x, y)
    # print(queue)

    # 뱀 이동
    time += 1
    x += int(dir_table[dir][0]) - 1
    y += int(dir_table[dir][1]) - 1

    # 충돌 여부 확인
    if x < 0 or x >= N or y < 0 or y >= N:
        print(time)
        break
    elif [x, y] in queue: # 이렇게 해도 된다!!!
        print(time)
        break

    # 사과 먹음 : 사이즈 커지기
    if board[y][x] == 1: # 행렬 순서 너무너무너무 헷갈린다!!!
        board[y][x] = 0
        size += 1

    # 현재 뱀 위치 저장 + 오래된 뱀 위치 제거
    queue.append([x, y])
    if len(queue) > size:
        queue.popleft()

    # 다음 방향 잡기
    if str(time) in time_dir:
        dir = dir_change(dir, time_dir[str(time)])


# ---------------------------------------------------
# 다른 사람 풀이 -> 나와 유사함
# ---------------------------------------------------
"""
n = int(input())
k = int(input())
zido = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    zido[x][y] = 1
l = int(input())
move = [list(map(str, input().split())) for _ in range(l)]
time = 1
x, y = 1, 1
index = 0
move_index = 0
dx_list = [1, 0, -1, 0]
dy_list = [0, 1, 0, -1]
dx = dx_list[move_index]
dy = dy_list[move_index]
body_length = 1
body = [[1, 1]]
while (True):
    if int(move[index][0]) == time - 1:
        if move[index][1] == 'D':
            if move_index + 1 > 3:
                move_index -= 3
            else:
                move_index += 1

        elif move[index][1] == 'L':
            if move_index - 1 < 0:
                move_index += 3
            else:
                move_index -= 1
        dx, dy = dx_list[move_index], dy_list[move_index]
        if index < l - 1: index += 1
    x += dx
    y += dy
    if x > n or y > n or x < 1 or y < 1:
        break
    if [x, y] in body:
        break
    body.append([x, y])
    if zido[y][x] != 1:
        body = body[1:]
    else:
        zido[y][x] = 0
    # print(time,body)
    time += 1
print(time)
"""
# ---------------------------------------------------