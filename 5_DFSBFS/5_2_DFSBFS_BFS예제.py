# 라이브러리 불러오기
from collections import deque

# 각 노드 연결 정보 선언 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드 방문 여부 (1차원 리스트)
visited = [False] * 9

# BFS 함수 정의
def bfs(graph, start, visited):
    # queue 선언
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # Queue 비워질 때까지 노드 방문
    while queue:
        # 가장 오래된 노드 1개 뽑기
        v = queue.popleft()
        print(v, end = ' ')

        # 가장 오래된 노드와 연결된 인접 노드 방문
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# BFS 함수 호출
bfs(graph, 1, visited)