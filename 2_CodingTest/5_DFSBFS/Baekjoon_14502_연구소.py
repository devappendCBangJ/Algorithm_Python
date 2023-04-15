# 라이브러리 불러오기
from itertools import combinations
from copy import deepcopy
from collections import deque

# 맵 크기 받기
N, M = list(map(int, input().split()))
base_board = []

# 변수 초기화
zero_count = 0
zero_index = []
two_index = []
comb_zero = []

# 맵 정보 받기
for board_y in range(N):
    # 인덱스 추출
    line = list(map(int, input().split()))
    for board_x in range(len(line)):
        # 2 인덱스
        if line[board_x] == 2:
            two_index.append([board_x, board_y])
        # 0 인덱스
        elif line[board_x] == 0:
            zero_index.append([board_x, board_y])
    base_board.append(line)

# 0 개수 추출
zero_count = len(zero_index)

# print(base_board)
# print(zero_count)
# print(two_index)
# print(zero_index)

# 벽 3개로 만들 수 있는 모든 조합 시도
for walls in combinations(zero_index, 3):
    # comb_board를 base_board 상태로 초기화
    comb_board = deepcopy(base_board)
    zero_count = len(zero_index) - 3 # 0 3개를 2로 만들었기 때문에, 기존 0개수 - 3

    # 벽 3개로 만들 수 있는 모든 조합 시도
    for wall_coor in walls:
        comb_board[wall_coor[1]][wall_coor[0]] = 1

    # 바이러스 BFS를 활용해서 하나씩 확산
    for virus_coor in two_index:
        # print(virus_coor)
        queue = deque([virus_coor])
        # print(queue)

        # 모든 queue 순회
        while queue:
            # queue에서 가장 오래된 공간 불러오기
            x, y = queue.popleft()

            # 벽, 바이러스가 아닌 공간만 방문
            for n_x, n_y in [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]:
                # print(n_x, n_y)
                if n_x < 0 or n_x >= M or n_y < 0 or n_y >= N:
                    continue
                elif comb_board[n_y][n_x] != 0:
                    continue
                else:
                    queue.append([n_x, n_y])
                    zero_count -= 1
                    comb_board[n_y][n_x] = 2 # 보통 BFS는 queue에서 원소 꺼내왔을 때, 방문 여부를 표시함!!!
    # 현재 조합에서의 zero 개수 list에 추가
    comb_zero.append(zero_count)
    # print(zero_count)

# zero 개수 최대일 때 개수
print(max(comb_zero))

# ---------------------------------------------------
# 다른 사람 풀이 -> 내가 더 효율적인 코드
# ---------------------------------------------------
"""
from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

def bfs():
    q = deque(Q)
    visited = [[0]*m for _ in range(n)]
    for k,l in q :
        visited[k][l] = 1

    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and temp[ni][nj] == 0 :
                visited[ni][nj] = 1
                temp[ni][nj] = 2
                q.append((ni,nj))

    cnt = 0
    for i in range(n) :
        for j in range(m):
            if temp[i][j] == 0 :
                cnt += 1
    return cnt

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [[0,1],[1,0],[0,-1],[-1,0]]
Q = []
check = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 :
            check.append((i,j))
        elif graph[i][j] == 2 :
            Q.append((i,j))

MAX = 0
for p in combinations(check,3):
    temp = deepcopy(graph)
    for row,col in p :
        temp[row][col] = 1
    ans = bfs()
    MAX = max(MAX,ans)

print(MAX)
"""
# ---------------------------------------------------