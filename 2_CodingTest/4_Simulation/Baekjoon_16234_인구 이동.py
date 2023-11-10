# 60min 소요

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, L, R = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

now_update = True
now_update_count = -1

# 모든 국가에서 주변 방문 가능 국가 탐색 + 인구수 업데이트
while now_update == True:
    now_update = False
    now_update_count += 1
    visited_board = [[0 for _ in range(N)] for _ in range(N)] # while문 돌 때마다 초기화 해줘야함!!!
    for r in range(N):
        for c in range(N):
            if visited_board[r][c] == 0:
                # 변수 초기화
                visited_board[r][c] = 1 # queue 초기값도 visited_board 업데이트 해줘야함!!!
                neighbor_sum = board[r][c]
                neighbor_coors = [[r, c]]
                queue = deque([[r, c]]) # r, c
                # 주변 방문 가능 국가 탐색
                while queue:
                    r, c = queue.popleft()
                    for dir in range(4):
                        nr = r + dr[dir]
                        nc = c + dc[dir]
                        if 0 <= nr <= N-1 and 0 <= nc <= N-1 and visited_board[nr][nc] == 0 and L <= abs(board[r][c] - board[nr][nc]) <= R:
                            visited_board[nr][nc] = 1 # 방문 표시
                            neighbor_sum += board[nr][nc] # 현재 국가로부터, 방문 가능 국가 인구수 총합
                            neighbor_coors.append([nr, nc]) # 현재 국가로부터, 방문 가능 국가 좌표 저장
                            queue.append([nr, nc]) # 다음 탐색 국가
                # 국경 개방 : 인구 수 업데이트
                if 2 <= len(neighbor_coors):
                    now_update = True # 인구 수 업데이트 count는 하루에 한 번만 해야함!!!
                    for nr, nc in neighbor_coors:
                        board[nr][nc] = neighbor_sum // len(neighbor_coors)
    print(board)

# 결과 출력
print(now_update_count)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 거의 완전히 똑같은데 왜 내껀 안되고, 이 코드는 되는거지
# https://resilient-923.tistory.com/353
# ---------------------------------------------------
import sys
input = sys.stdin.readline
from collections import deque

graph = []
n,l,r = map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp
            
result = 0
while 1:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
                if len(country) > 1:
                    flag = 1
                    # 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x,y in country:
                        graph[x][y] = number
    # 연합을 해체하고, 모든 국경선을 닫는다.
    if flag == 0:
        break
    result += 1
print(result)
"""