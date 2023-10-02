# 240min 소요

N, M, k = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 상어 정보 저장
shark_list = [-1 for _ in range(M)]
smell_board = [[[-1, 0] for _ in range(N)] for _ in range(N)]
shark_board = [[-1 for _ in range(N)] for _ in range(N)]
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c] != 0:
            shark_list[line[c]-1] = [r, c, 0] # 문제에서 주어진 상어 idx보다 1 작음
            shark_board[r][c] = line[c]-1
            smell_board[r][c] = [line[c]-1, k]
for idx, dir in enumerate(list(map(int, input().split()))):
    shark_list[idx][2] = dir - 1
    
# 방향 우선순위 저장
dir_list = [[] for _ in range(M)]
for m in range(M):
    for _ in range(4):
        line = list(map(int, input().split()))
        dir_list[m].append([dir - 1 for dir in line])

# 상어 활동 시작
time = 1
while time <= 1001: # 초기 시간이 0초이고, 한바퀴 돌고나면 1초가 지남. 문제에서 1000초가 넘어도 다른 상어가 격자에 남아있으면 -1 출력이니까 1001초 돌려보고 안되면 break 하라는 뜻인듯
    # 각각의 상어에 대한 활동
    # print("shark_board1 : ", shark_board)
    # print("smell_board1 : ", smell_board)
    for sidx in range(len(shark_list)):
        if shark_list[sidx] != -1:
            sr, sc, sdir = shark_list[sidx]
            # 다음 경로에 아무것도 없을 때 (다음 step에 다른 상어가 없는 경우 / 있는 경우) : 이동
            temp_didx = 1000000000
            moved = False
            for didx, ndir in enumerate(dir_list[sidx][sdir]):
                nr = sr + dr[ndir]
                nc = sc + dc[ndir]
                if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                    if smell_board[nr][nc][1] == 0:
                        moved = True
                        shark_board[sr][sc] = -1
                        if shark_board[nr][nc] == -1: # 상어가 있으면서 냄새가 없는 경우도 바로 break 해줘야함!!!
                            shark_list[sidx] = [nr, nc, ndir]
                            shark_board[nr][nc] = sidx
                        else:
                            origin_sidx = shark_board[nr][nc]
                            if sidx < origin_sidx:
                                if didx < temp_didx:
                                    shark_list[origin_sidx] = -1
                                    shark_list[sidx] = [nr, nc, ndir]
                                    shark_board[nr][nc] = sidx
                                    temp_didx = didx
                            else:
                                shark_list[sidx] = -1
                                # print(shark_list)
                        break # 다음 위치에 냄새가 없는 경우, 무조건 그곳으로 이동!!!
            # 다음 경로에 냄새가 존재할 때 : 나의 냄새인 경우만 이동
            if moved == False:
                for didx, ndir in enumerate(dir_list[sidx][sdir]):
                    nr = sr + dr[ndir]
                    nc = sc + dc[ndir]
                    if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                        if smell_board[nr][nc][0] == sidx and smell_board[nr][nc][1] != 0:
                            shark_list[sidx] = [nr, nc, ndir]
                            shark_board[sr][sc] = -1
                            shark_board[nr][nc] = sidx
                            break
    # 냄새 업데이트
    shark_count = 0
    for r in range(N):
        for c in range(N):
            if 0 <= shark_board[r][c]:
                smell_board[r][c] = [shark_board[r][c], k]
                shark_count += 1
            elif 0 <= smell_board[r][c][0]:
                smell_board[r][c][1] -= 1
                if smell_board[r][c][1] == 0:
                    smell_board[r][c][0] = -1
    # print(f"[time] shark_board : [{time}] {shark_board}")
    # print(f"[time] shark_list : [{time}] {shark_list}")
    # print(f"[time] smell_board : [{time}] {smell_board}")

    # time 증가
    if shark_count != 1: # shark count가 0이 아니라, 1일때 끝남!!!
        time += 1
    else:
        break
if 1001 <= time:
    print(-1)
else:
    print(time)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 나와 풀이 거의 유사함. 죽은 상어가 있는지 확인하는 부분이 내 방식보다 비효율적 but 함수화를 통해 정리해둬서 가독성이 좋음
# https://seongonion.tistory.com/122
# ---------------------------------------------------
import sys
input = sys.stdin.readline
# 1번 상어는 모두 쫓아낼 수 있음
# N * N 그래프에 M 마리의 상어, k = 냄새 지속시간
n, m, k = map(int, input().split())
graph = []
sharks = [[] for _ in range(m + 1)]

# 위, 아래, 왼쪽, 오른쪽
moves = [
    [],
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            sharks[row[j]].append([i, j])
    
    graph.append(row)

current_d_list = list(map(int, input().split()))

for i in range(1, m + 1):
    sharks[i].append(current_d_list[i - 1])

sharks_preference = {}
for i in range(1, m + 1):
    sharks_preference[i] = [0]
    for j in range(1, 5):
        sharks_preference[i].append(list(map(int, input().split())))

# sharks[i][0]: i번째 상어의 현재 위치
# sharks[i][1]: i번째 상어가 현재 바라보는 방향
# 
# sharks_preference[i][j]: i번째 상어가 j방향을 보고 있을 때 방향 우선순위 리스트

# stage
# 1. 움직인다. (냄새 정보 확인) 
# 아무 냄새가 없는 칸으로 먼저 이동 / 자신의 냄새가 있는 칸으로 (가능한 칸이 여러개일 경우 우선순위를 따름)
# 2. 겹치는지 확인한다. (죽는 상어가 있는지 확인)
# 3. 냄새를 기록 및 업데이트한다.

graph_smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# 첫 냄새 기록
for i in range(1, m + 1):
    graph_smell[sharks[i][0][0]][sharks[i][0][1]][0], graph_smell[sharks[i][0][0]][sharks[i][0][1]][1] = i, k


# 내 냄새가 있는 방향 확인
def my_smell_check(graph_smell, shark_num):
    current_shark_loc = sharks[shark_num][0]
    current_shark_d = sharks[shark_num][1]
    preferences = sharks_preference[shark_num][current_shark_d]

    for direction in preferences:
        x, y = current_shark_loc[0] + moves[direction][0], current_shark_loc[1] + moves[direction][1]

        if 0 <= x < n and 0 <= y < n:
            if graph_smell[x][y][0] == shark_num:

                return [x, y, direction]

# 비어있는 공간 확인
def empty_check(graph_smell, shark_num):
    current_shark_loc = sharks[shark_num][0]
    current_shark_d = sharks[shark_num][1]
    preferences = sharks_preference[shark_num][current_shark_d]

    for preference in preferences:
        x, y = current_shark_loc[0] + moves[preference][0], current_shark_loc[1] + moves[preference][1]

        if 0 <= x < n and 0 <= y < n:
            if graph_smell[x][y][0] == 0:
                return [x, y, preference]
    
    # 빈 곳이 없으면 False 리턴
    return False
    
# 죽는 상어가 있는지 확인
def check_shark_dead():
    dead_num = 0
    for i in range(1, m):
        if sharks[i][0] == -1:
            continue

        for j in range(i + 1, m + 1):
            if sharks[j][0] == -1:
                continue
            
            i_shark_loc = sharks[i][0]
            j_shark_loc = sharks[j][0]

            if i_shark_loc == j_shark_loc:
                dead = max(i, j)
                sharks[dead][0] = -1
                dead_num += 1
    
    return dead_num

# 살아있는 상어의 수
remain_shark = m
# 이동 횟수
ans = 0
# 현재 상어위치 기록 (냄새 기록을 위한 위치)
current_loc_shark = [[0, 0]] * (m + 1)

while remain_shark > 1 and ans < 1001:
    # 상어 움직임
    for i in range(1, m + 1):
        # 현재 상어가 죽어있다면 건너뜀
        if sharks[i][0] == -1:
            continue

        current_loc = sharks[i][0]
        current_loc_shark[i] = current_loc
        empty_move = empty_check(graph_smell, i)

        # 비어있는 곳부터 탐색
        if empty_move:
            # 비어있는 곳 중 이동할 곳이 있다면 해당 위치로 이동 후 sharks 리스트 업데이트
            new_loc_x, new_loc_y, new_d = empty_move[0], empty_move[1], empty_move[2]
            sharks[i][0][0], sharks[i][0][1] = new_loc_x, new_loc_y
            sharks[i][1] = new_d
        
        else:
            # 비어있는 곳 없을 때 자신의 냄새 있는 곳 탐색, 이동 후 sharks 리스트 업데이트
            smell_move = my_smell_check(graph_smell, i)
            new_loc_x, new_loc_y, new_d = smell_move[0], smell_move[1], smell_move[2]
            sharks[i][0][0], sharks[i][0][1] = new_loc_x, new_loc_y
            sharks[i][1] = new_d

    # 죽은 상어 있는지 확인 후 업데이트
    dead_num = check_shark_dead()
    remain_shark -= dead_num

    # 기존 존재하던 냄새 업데이트 (1 빼줌)
    for i in range(n):
        for j in range(n):
            if graph_smell[i][j][0] != 0:
                graph_smell[i][j][1] -= 1
            
            if graph_smell[i][j][1] == 0:
                graph_smell[i][j][0] = 0

    # 살아있는 상어에 대하여 새로운 냄새 생성
    for i in range(1, m + 1):
        if sharks[i][0] != -1:
            x, y = current_loc_shark[i][0], current_loc_shark[i][1]
            graph_smell[x][y] = [i, k]
    
    ans += 1

if ans > 1000:
    print(-1)
else:
    print(ans)
"""