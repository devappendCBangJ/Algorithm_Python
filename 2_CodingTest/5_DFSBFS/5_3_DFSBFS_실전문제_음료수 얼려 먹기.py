# # 라이브러리 불러오기
# from collections import deque
#
# # input 받기
# graph = []
# frame_size = map(int, input().split())
# h, w = frame_size # 행렬 순서 너무너무너무 헷갈린다!!!
# for _ in range(h):
#    graph.append(input().split())
# print(graph)
#
# # 변수 선언
# count = 0
#
# # BFS 함수 선언
# def bfs(start_x, start_y):
#     # queue 생성
#     queue = deque([[start_x, start_y]])
#     # 방문한 노드 체크
#     graph[start_y][start_x] = '2' # 행렬 순서 너무너무너무 헷갈린다!!!
#     # queue 내부 원소 사라질 때까지 순회
#     while queue:
#         # 가장 오래된 노드 1개 빼기
#         x, y = queue.popleft()
#
#         # 탐색할 이웃 인덱스 구하기 + 이웃이 탐색되지 않은 노드인 경우, 탐색
#         for neighbor_x, neighbor_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
#             if neighbor_x < 0 or neighbor_x >= w or neighbor_y < 0 or neighbor_y >= h:
#                 continue
#             if graph[neighbor_y][neighbor_x] == '0':
#                 queue.append([neighbor_x, neighbor_y])
#                 graph[neighbor_y][neighbor_x] = '2'  # 행렬 순서 너무너무너무 헷갈린다!!!
#         # print(queue)
#     # print(graph)
#
# # frame 전부 순회
# for x in range(w): # 행렬 순서 너무너무너무 헷갈린다!!!
#     for y in range(h):
#         if graph[y][x] == '0': # 행렬 순서 너무너무너무 헷갈린다!!!
#             bfs(x, y)
#             count += 1
#
# print(count)

# ---------------------------------------------------
# 교재 풀이 -> DFS 구현
# ---------------------------------------------------
"""
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M: # 어차피 재귀이고, x와 y는 함수 들어올 때 정해졌기 때문에, 다른 이웃은 다른 함수에서 처리함. 그래서 그냥 return 해도돰!!!
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 표시!!!

        dfs(x-1, y) # DFS 방문!!!
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True: # 하나라도 방문한 경우 : count!!!
            result += 1

print(result)
"""