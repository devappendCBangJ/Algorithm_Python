N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# print(board)

flag = 0
count = 0
dx = [0, 1, 0, -1] # 반시계 이동 주의!
dy = [-1, 0, 1, 0]

while flag == 0:
    moved = False
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1
    for _ in range(4):
        d = (d - 1) % 4
        if 0 <= r + dy[d] < N and 0 <= c + dx[d] < M and board[r + dy[d]][c + dx[d]] == 0:
            r += dy[d]
            c += dx[d]
            moved = True
            break
    if moved == False:
        if 0 <= r - dy[d] < N and 0 <= c - dx[d] < M and board[r - dy[d]][c - dx[d]] != 1: # 이동할 곳이 쓰레기를 이미 치운 곳이여도 이동 가능! 단, 벽인 경우는 이동 불가능!
            r -= dy[d]
            c -= dx[d]
        else:
            break
    # for b in board:
    #     print(b)
    # print("")
print(count)

# ---------------------------------------------------
# 다른 사람 풀이 -> 풀이 방식 같음
# https://resilient-923.tistory.com/164
# ---------------------------------------------------
"""
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]
"""