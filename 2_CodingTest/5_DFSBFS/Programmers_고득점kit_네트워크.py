# 입력 받기
n = int(input())
computers = []
for _ in range(n):
    computers.append(list(map(int, input().split())))

# 초기화
counts = [0 for _ in range(n)]

def dfs(r_idx, count):
    for c_idx in range(n):
        if computers[r_idx][c_idx] == 1 and counts[c_idx] == 0:
            counts[c_idx] = count
            dfs(c_idx, count)

# DFS
for r_idx in range(n): # DFS의 시작점의 개수는 Row개!!!
    count = max(counts) + 1
    dfs(r_idx, count)

# 결과 출력
print(counts)
print(max(counts))

# ---------------------------------------------------
# 다른 사람 풀이 -> row를 방문했었는지 확인하고, 방문하지 않았던 row를 방문할때만 result++ 해주면 되네
# ---------------------------------------------------
"""
# 입력 받기
n = int(input())
computers = []
for _ in range(n):
    computers.append(list(map(int, input().split())))

# DFS 방문
def visit(r_idx, computers, visited):
    visited[r_idx] = 1
    for c_idx in range(n):
        if visited[c_idx] == 0 and computers[r_idx][c_idx] == 1:
            visit(c_idx, computers, visited)

def solution(n, computers):
    # 방문 여부 확인
    visited = [0] * n
    answer = 0

    # row 기준으로, 방문하지 않은 Computer 하나씩 방문
    for r_idx in range(n):
        if visited[r_idx] == 0:
            visit(r_idx, computers, visited)
            answer += 1
        if 0 not in visited:
            break

    return answer

# 결과 출력
print(solution(n ,computers))
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> BFS로도 가능
# ---------------------------------------------------
"""
# 입력 받기
n = int(input())
computers = []
for _ in range(n):
    computers.append(list(map(int, input().split())))

def solution(n, computers):
    # BFS 방문
    def BFS(node, visit): # 일반적인 BFS처럼 해도 되네!!!
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0

    # row 기준으로, 방문하지 않은 Computer 하나씩 방문
    for i in range(n):
        try: # visit 내에 값이 0인 원소가 없을 경우 except로 넘어감 -> for문을 n번 다 못돌고 끝나는 경우가 대부분!!!
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer
    
# 결과 출력
print(solution(n ,computers))
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> DFS를 stack으로 구현
# ---------------------------------------------------
"""
# 입력 받기
n = int(input())
computers = []
for _ in range(n):
    computers.append(list(map(int, input().split())))

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    # DFS 방문
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)

    # row 기준으로, 방문하지 않은 Computer 하나씩 방문
    i = 0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

# 결과 출력
print(solution(n ,computers))
"""