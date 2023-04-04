# 라이브러리 불러오기
from collections import deque

# 변수 초기화
times = 0
done = [0]*100001

# input 불러오기
N, K = map(int, input().split())

# BFS 함수 정의
def bfs(start_N, times):
    # queue 선언
    queue = deque([[start_N, times]])

    # queue 원소 없을 때까지 순회
    while queue:
        # 오래된 노드부터 하나씩 빼기
        N, times = queue.popleft()

        print(N, times)

        # N을 2배 했을 때 K의 2배 보다 작은 경우 + 방문하지 않은 경우 : 2배 해보기
        if N < 2 * K:
            tmp = 2 * N
            if tmp == K:
                return times + 1
            if 0 <= tmp <= 100000 and done[tmp] == 0:
                queue.append([tmp, times + 1])
                done[tmp] = 1
        # 2배 하면 큰 경우 + 방문하지 않은 경우 : 뒤로 가기
        if 2 * N > K:
            tmp = N - 1
            if tmp == K:
                return times + 1
            if 0 <= tmp <= 100000 and done[tmp] == 0:
                queue.append([tmp, times + 1])
                done[tmp] = 1
        # 2배 하면 작거나 같은 경우 + 이전에 방문하지 않은 경우 : 앞으로 가기
        else:
            tmp = N + 1
            if tmp == K:
                return times + 1
            if 0 <= tmp <= 100000 and done[tmp] == 0:
                queue.append([tmp, times + 1])
                done[tmp] = 1

print(bfs(N, times))

# ---------------------------------------------------
# 다른 사람 풀이 -> 코드 짧고, 수행시간 2배 단축
# ---------------------------------------------------
"""
from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX

def BFS(N):
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        N = q.popleft()
        if N == K:
            return visited[N]
        for num in (N - 1, N + 1, N * 2):
            if 0 <= num < MAX and visited[num] == 0:
                visited[num] = visited[N] + 1
                q.append(num)
print(BFS(N))
"""
# ---------------------------------------------------