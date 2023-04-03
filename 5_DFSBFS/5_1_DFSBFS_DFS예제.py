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

# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')

    # 현재 노드와 연결된 노드 DFS 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# DFS 함수 호출
dfs(graph, 1, visited)