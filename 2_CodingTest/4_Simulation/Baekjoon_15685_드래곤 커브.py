N = int(input())
curves = []
for _ in range(N):
    curves.append(list(map(int, input().split())))

board = [[0 for _ in range(101)] for _ in range(101)] # 실제 문제에서 주어진 Grid는 101개이고, 우리가 생각하는 배열의 순서와 같다!

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in curves:
    temp_curves = [[x, y]]
    for i in range(g+1):
        if i == 0:
            if 0 <= x + dx[d] < 101 and 0 <= y + dy[d] < 101: # N은 Grid 크기가 아니라, 드래곤 커브의 개수이다!
                temp_curves.append([x + dx[d], y + dy[d]])
        else:
            base_x, base_y = temp_curves[-1]
            temp_curves.extend([[base_x + (base_y - n_y), base_y - (base_x - n_x)] for n_x, n_y in reversed(temp_curves[:-1]) if 0 <= base_x + (base_y - n_y) < 101 and 0 <= base_y - (base_x - n_x) < 101]) # temp_curves[:-1:-1] 이렇게 하니까 안되네?  # N은 Grid 크기가 아니라, 드래곤 커브의 개수이다! # 실제 문제에서 주어진 Grid는 101개이고, 우리가 생각하는 배열의 순서와 같다!
            # new_temp_curves = list(map(lambda n_x, n_y: [base_x + (base_y - n_y), base_y - (base_x - n_x)], temp_curves[:-1]))
    # print(temp_curves)
    for x, y in temp_curves:
        board[y][x] = 1

count = 0
for x in range(101-1):
    for y in range(101-1):
        if board[y][x] == 1 and board[y][x+1] == 1 and board[y+1][x] == 1 and board[y+1][x+1] == 1:
            count += 1
print(count)

# ---------------------------------------------------
# 다른 사람 풀이 -> 규칙을 찾아내서 방향을 구함!
# https://kyun2da.github.io/2021/04/06/dragonCurve/
# ---------------------------------------------------
"""
import sys

input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브들이 모일 배열 1이면 드래곤 커브의 일부
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    # x, y : 드래곤 커브 시작점, d : 시작 방향, g : 세대
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    move = [d]
    # g 세대 만큼 반복
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    # 드래곤 커브에 해당하는 좌표 arr에 추가
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구하기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            ans += 1

print(ans)
"""