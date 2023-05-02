# 라이브러리 불러오기
from collections import deque

# input 불러오기
maze = []
N, M = map(int, input().split())
for i in range(N):
    maze.append([i for i in input()])
    # print(maze)

# BFS 함수 정의
def bfs(start_x, start_y):
    # queue 생성
    queue = deque([[start_x, start_y, 1]])

    # 방문한 노드 체크
    maze[start_y][start_x] = '2'

    # queue 내부 원소 사라질 때까지 순회
    while queue:
        # 가장 오래된 노드부터 1개씩 꺼내기
        x, y, dis = queue.popleft()

        # 탐색할 이웃 인덱스 구하기 + 이웃이 탐색되지 않은 노드인 경우, 탐색 + dis 증가
        for neighbor_x, neighbor_y in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if neighbor_x < 0 or neighbor_x >= M or neighbor_y < 0 or neighbor_y >= N:
                continue
            if maze[neighbor_y][neighbor_x] == '1':
                maze[neighbor_y][neighbor_x] = '2'
                queue.append([neighbor_x, neighbor_y, dis + 1])

                # 목적지 다다를 시, dis 출력
                if neighbor_x == M-1 and neighbor_y == N-1:
                    print(dis + 1)
                    return True

# BFS
bfs(0, 0)

