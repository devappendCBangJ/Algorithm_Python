from collections import deque

N, M = list(map(int, input().split()))
board = []
blue_red = [[[], [], 0]] # BFS 돌면서 time도 지속적으로 기억해야함!

for n in range(N):
    board.append([s for s in input()])
# print(board)
for n in range(N):
    for m in range(M):
        if board[n][m] == "B":
            blue_red[0][0] = [n, m]
            board[n][m] = '.' # board에서도 blue와 red의 위치를 계속해서 업데이트 해야되는데, BFS 순회마다 달라지므로, 번거로움을 덜기 위해 queue에서만 기억!
        elif board[n][m] == "R":
            blue_red[0][1] = [n, m]
            board[n][m] = '.'
# print(blue_red)

visited = [] # 간단하게 방문 여부 확인 가능!

dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

result = 0

def red_blue_first(i, red_n, red_m, blue_n, blue_m, rb, time):
    global result
    if rb == "r":
        while 1 <= red_n + dn[i] < N - 1 and 1 <= red_m + dm[i] < M - 1 and board[red_n + dn[i]][red_m + dm[i]] != '#' and (red_n + dn[i] != blue_n or red_m + dm[i] != blue_m): # board에서도 blue와 red의 위치를 계속해서 업데이트 해야되는데, BFS 순회마다 달라지므로, 번거로움을 덜기 위해 queue에서만 기억!
            red_n += dn[i]
            red_m += dm[i]
            if board[red_n][red_m] == 'O':
                result = time + 1
        while 1 <= blue_n + dn[i] < N - 1 and 1 <= blue_m + dm[i] < M - 1 and board[blue_n + dn[i]][blue_m + dm[i]] != '#' and (blue_n + dn[i] != red_n or blue_m + dm[i] != red_m):
            blue_n += dn[i]
            blue_m += dm[i]
            if board[blue_n][blue_m] == 'O':
                result = 0
                return -1, -1, -1, -1
    else:
        while 1 <= blue_n + dn[i] < N - 1 and 1 <= blue_m + dm[i] < M - 1 and board[blue_n + dn[i]][blue_m + dm[i]] != '#' and (blue_n + dn[i] != red_n or blue_m + dm[i] != red_m):
            blue_n += dn[i]
            blue_m += dm[i]
            if board[blue_n][blue_m] == 'O':
                return -1, -1, -1, -1
        while 1 <= red_n + dn[i] < N - 1 and 1 <= red_m + dm[i] < M - 1 and board[red_n + dn[i]][red_m + dm[i]] != '#' and (red_n + dn[i] != blue_n or red_m + dm[i] != blue_m):
            red_n += dn[i]
            red_m += dm[i]
            if board[red_n][red_m] == 'O':
                result = time + 1
    return red_n, red_m, blue_n, blue_m

queue = deque(blue_red)
while queue:
    blue, red, time = queue.popleft()
    if time == 10: # 이번 time에서 목적지에 도착하지 못했으므로, 다음 time이 도달하는 시점은 11이 될 것임 -> 조기 종료!
        result = -1
    if result != 0: # 조기 종료인 경우 끝내기!
        break
    blue_n, blue_m = blue
    red_n, red_m = red
    for i in range(4):
        if board[red_n + dn[i]][red_m + dm[i]] != '#' or board[blue_n + dn[i]][blue_m + dm[i]] != '#' and (red_n + dn[i] != blue_n or red_m + dm[i] != blue_m) and (blue_n + dn[i] != red_n or blue_m + dm[i] != red_m):
            if i == 0 and blue_n >= red_n: # 파란색, 빨간색 공 전부 무조건 이동 시킨 후에, 두개 좌표가 같으면 더 많이 움직인 공을 한칸 뒤로 보내면 더 쉽대요!
                next_red_n, next_red_m, next_blue_n, next_blue_m = red_blue_first(i, red_n, red_m, blue_n, blue_m, "r", time)
            elif i == 1 and red_m >= blue_m:
                next_red_n, next_red_m, next_blue_n, next_blue_m = red_blue_first(i, red_n, red_m, blue_n, blue_m, "r", time)
            elif i == 2 and red_n >= blue_n:
                next_red_n, next_red_m, next_blue_n, next_blue_m = red_blue_first(i, red_n, red_m, blue_n, blue_m, "r", time)
            elif i == 3 and blue_m >= red_m:
                next_red_n, next_red_m, next_blue_n, next_blue_m = red_blue_first(i, red_n, red_m, blue_n, blue_m, "r", time)
            else:
                next_red_n, next_red_m, next_blue_n, next_blue_m = red_blue_first(i, red_n, red_m, blue_n, blue_m, "b", time)

            if result != 0: # 조기 종료인 경우 끝내기!
                break
            if next_red_n == -1 and next_red_m == -1 and next_blue_n == -1 and next_blue_m == -1: # blue 공이 들어간 경우 순회 취소!
                continue
            if [next_red_n, next_red_m, next_blue_n, next_blue_m] not in visited: # 간단하게 방문 여부 확인 가능!
                visited.append([next_red_n, next_red_m, next_blue_n, next_blue_m])
                queue.append([[next_blue_n, next_blue_m], [next_red_n, next_red_m], time+1])
if result == 0: # 10time 돌기도 전에 모든 경우의 수를 다 순회한 경우!
    result = -1
# print(board)
print(result)