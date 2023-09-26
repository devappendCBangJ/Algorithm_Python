# 210min 소요

from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
goals = []
for _ in range(m):
    goals.append(list(map(int, input().split())))
# print(goals)

def move():
    global count # 일반적인 단일 변수는 전역변수 선언하지 않으면, 함수 내에서 값을 바꿔도 바깥에는 반영이 안됨!!!
    for hi, human in enumerate(next_coors):
        new_next_coors = []
        up_count = False
        for r, c in human:
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                    if hi not in visited_boards[nr][nc] and board[nr][nc] != 2:
                        visited_boards[nr][nc].add(hi)
                        new_next_coors.append([nr, nc]) # 배열 차원 헷갈림!!!
                        if goal_coors[hi] == [nr, nc]:
                            new_next_coors = []
                            board[nr][nc] = 2
                            up_count = True
                            count += 1
                            if count == m:
                                return True
                            break
            if up_count == True:
                break
        next_coors[hi] = new_next_coors

def load_human():
    if time <= len(goals):
        gr, gc = goals[time-1]
        queue = deque([[gr-1, gc-1]]) # 문제에서 제시한 좌표와 내가 만든 배열의 좌표를 맞춰줘야함!!!
        human_visited_board = [[0 for _ in range(n)] for _ in range(n)] # move에서 BFS 쓸 때는 visited 생각해놓고, load_human에서 BFS 쓸 때 visited 고려 안하면 시간 + 메모리 터짐!!!
        while queue:
            r, c = queue.popleft()
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr <= n-1 and 0 <= nc <= n-1 and human_visited_board[nr][nc] == 0:
                    if board[nr][nc] == 0:
                        queue.append([nr, nc])
                        human_visited_board[nr][nc] = 2
                    elif board[nr][nc] == 1:
                        board[nr][nc] = 2
                        next_coors.append([[nr ,nc]])
                        goal_coors.append([gr-1, gc-1]) # 문제에서 제시한 좌표와 내가 만든 배열의 좌표를 맞춰줘야함!!!
                        visited_boards[nr][nc].add(len(goal_coors)-1)
                        return

time = 0
count = 0
next_coors = []
goal_coors = []
visited_boards = [[set() for _ in range(n)] for _ in range(n)]
# print(visited_boards)
while time < 60:
    time += 1
    result = move()
    if result:
        break
    load_human()
print(time)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 시간복잡도 비효율적 but 메모리 효율적
# https://velog.io/@mimmimmu/18%EC%A3%BC%EC%B0%A8-%EC%BD%94%EB%93%9C%ED%8A%B8%EB%A6%AC-%EC%82%BC%EC%84%B1%EA%B8%B0%EC%B6%9C-%EC%BD%94%EB%93%9C%ED%8A%B8%EB%A6%AC-%EB%B9%B5-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# ---------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split()) # 격자크기, 사람수
arr = [[0 for _ in range(n+1)]] # 격자 정보
base = []

for i in range(1, n+1):
    temp = [0]+list(map(int, input().strip().split()))
    for j in range(1, n+1):
        if temp[j]==1:
            base.append((i,j))
    arr.append(temp)

store = [list(map(int, input().strip().split())) for _ in range(m)]

cant_go = [[0 for _ in range(n+1)] for _ in range(n+1)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0] # 위, 왼, 오, 아

# 각 편의점과 각 베이스와 거리 구하기
def store_base(x, y, bx, by):
    q = deque()
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

    q.append((x, y))
    visited[x][y] = 1

    while q:
        px, py = q.popleft()
        if px == bx and py == by:
            return visited[px][py]-1
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if 1<=nx<n+1 and 1<=ny<n+1 and not visited[nx][ny] and not cant_go[nx][ny]:
                visited[nx][ny] = visited[px][py]+1
                q.append((nx,ny))
    return -1

# 편의점과 가장 가까운 베이스 구하기
def find_base(sx, sy):
    temp = []

    # 모든 베이스에 대해 store_base 함수 호출해서 거리를 구한다음에 규칙에 맞게 정렬해준다
    for bx, by in base:                                     # BFS 돌리면 되는데 왜 모든 베이스와의 거리를 구하는거지. 비효율적인 듯!!!
        if not cant_go[bx][by]:
            dis = store_base(sx, sy, bx, by)
            
            if dis!=-1:
                temp.append((dis, bx, by))
    
    if temp:
        temp.sort(key=lambda x:(x[0], x[1], x[2]))
        return temp[0][1], temp[0][2]
    else:
        return -1, -1

# 사람위치에서부터 편의점 위치까지 최단거리로 이동할 수 있는 "다음 홉"을 구하는 함수
def go_store(x, y, sx, sy, d):
    q = deque()
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y] = 1

    # 다음 홉부터 탐색 진행
    nx, ny = x+dx[d], y+dy[d]
    first_nx, first_ny = nx, ny
    if 1<=nx<n+1 and 1<=ny<n+1 and not cant_go[nx][ny]:
        visited[nx][ny] = 2
        q.append((nx, ny))
    # 다음 홉이 갈 수 없는 곳이면 sys.maxsize를 dis로 반환
    else:
        return sys.maxsize, 0, 0

    while q:
        px, py = q.popleft()
        # 편의점까지 도착했으면 거리, 다음홉 x, y를 반환
        if px==sx and py==sy:
            return visited[px][py]-1, first_nx, first_ny    # 각각 사람의 현재 위치에서 편의점 위치까지 도착할 수 있는 경우, 사람 현재 위치에서 바로 다음 칸의 좌표로 이동 -> 요렇게 해도 되네 ㄷㄷ!!!
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 1<=nx<n+1 and 1<=ny<n+1 and not cant_go[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[px][py]+1
                q.append((nx, ny))

    # 해당 방향을 다음홉으로 삼았을 때 편의점까지 갈 수 없는 경우
    return sys.maxsize, 0, 0

pos_list = [[] for _ in range(m)] # 사람의 현위치
t = 1 # 시간

# 가장 처음은 3단계부터 시작한다 (그전에는 맵에 아무도 없으니까)
sx, sy = store[0] 
bx, by = find_base(sx, sy)
pos_list[0] = [bx, by]
cant_go[bx][by] = 1

stop = [0 for _ in range(m)] # 편의점에 도착한 사람은 stop해줌
count = 0 # 편의점 도달한 사람 수
while count < m:
    t += 1
    temp_go = [(0,0) for _ in range(m)] # 사람별로 갈 다음 홉
    for i in range(m):
        # 현재 맵에 i번째 사람이 있고 편의점까지 도착하지 않은 경우
        if pos_list[i] and not stop[i]:
            sx, sy = store[i]
            x, y = pos_list[i]
            min_dis = sys.maxsize
            min_fx, min_fy = 0, 0
            # 각 방향 별로 거리를 구해서 최단거리로 이동할 수 있는 방향(다음 홉 위치)을 구한다
            for d in range(4):                  # 왜 4방향을 나누는지 모르겠음. 그냥 방향 지정안하고 바로 탐색해도 될텐데!!!
                dis, fx, fy = go_store(x, y, sx, sy, d)
                if min_dis > dis:
                    min_dis = dis
                    min_fx, min_fy = fx, fy

            temp_go[i] = (min_fx, min_fy)       # 각각 사람의 현재 위치에서 편의점 위치까지 도착할 수 있는 경우, 사람 현재 위치에서 바로 다음 칸의 좌표로 이동 -> 요렇게 해도 되네 ㄷㄷ!!!
    
    for i, (fx, fy) in enumerate(temp_go):
        # 만약 한칸 이동했는데 도착한 경우 => 이동할 수 없는 칸으로 바꾸고 그 사람 stop시키고 도착완료한 사람 수 up
        if store[i][0]==fx and store[i][1]==fy:
            pos_list[i] = [fx, fy]
            cant_go[fx][fy] = 1
            stop[i] = 1
            count += 1
        # 도착한 거 아니면 그냥 이동만
        else:
            pos_list[i] = [fx, fy]

    # 3단계
    if t<=m:
        bx, by = find_base(store[t-1][0], store[t-1][1])
        pos_list[t-1] = [bx, by]
        cant_go[bx][by] = 1
        
print(t)
"""

"""
# ---------------------------------------------------
# 또다른 나의 풀이 -> 모든 사람에 대한 visited board를 관리하므로, set보다 많은 시간 + 메모리가 소요될 듯
# ---------------------------------------------------
from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
goals = []
for _ in range(m):
    goals.append(list(map(int, input().split())))
# print(goals)

def move():
    global count # 일반적인 단일 변수는 전역변수 선언하지 않으면, 함수 내에서 값을 바꿔도 바깥에는 반영이 안됨!!!
    for hi, human in enumerate(next_coors):
        new_next_coors = []
        up_count = False
        for r, c in human:
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                    if move_visited_boards[hi][nr][nc] == 0 and board[nr][nc] != 2:
                        move_visited_boards[hi][nr][nc] = 2
                        new_next_coors.append([nr, nc]) # 배열 차원 헷갈림!!!
                        if goal_coors[hi] == [nr, nc]:
                            new_next_coors = []
                            board[nr][nc] = 2
                            up_count = True
                            count += 1
                            if count == m:
                                return True
                            break
            if up_count == True:
                break
        next_coors[hi] = new_next_coors

def load_human():
    if time <= len(goals):
        gr, gc = goals[time-1]
        queue = deque([[gr-1, gc-1]]) # 문제에서 제시한 좌표와 내가 만든 배열의 좌표를 맞춰줘야함!!!
        human_visited_board = [[0 for _ in range(n)] for _ in range(n)] # move에서 BFS 쓸 때는 visited 생각해놓고, load_human에서 BFS 쓸 때 visited 고려 안하면 시간 + 메모리 터짐!!!
        while queue:
            r, c = queue.popleft()
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr <= n-1 and 0 <= nc <= n-1 and human_visited_board[nr][nc] == 0:
                    if board[nr][nc] == 0:
                        queue.append([nr, nc])
                        human_visited_board[nr][nc] = 2
                    elif board[nr][nc] == 1:
                        board[nr][nc] = 2
                        next_coors.append([[nr ,nc]])
                        goal_coors.append([gr-1, gc-1]) # 문제에서 제시한 좌표와 내가 만든 배열의 좌표를 맞춰줘야함!!!
                        move_visited_boards.append([[0 for _ in range(n)] for _ in range(n)]) # 굳이 board를 복사할 필요 없이, 전부 0으로 바꿔주면 됨!!!
                        move_visited_boards[-1][nr][nc] = 2
                        return

time = 0
count = 0
next_coors = []
goal_coors = []
move_visited_boards = []
while True:
    time += 1
    result = move()
    if result:
        break
    load_human()
print(time)
"""