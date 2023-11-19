from collections import deque

N, K = map(int, input().split())

def bfs(N):
    queue = deque([N])
    dists[N] = 0
    while queue:
        N = queue.popleft()
        if N == K:
            return dists[N]
        for nN in [2 * N, N - 1, N + 1]: # N+1보다 N-1을 먼저 탐색해야함. 순서 매우매우매우 중요!!!
            if 0 <= nN <= end_idx and dists[nN] == -1:
                if nN == 2 * N:
                    dists[nN] = dists[N]
                    queue.appendleft(nN)
                else:
                    dists[nN] = dists[N] + 1
                    queue.append(nN)

if K <= N:
    print(N-K)
else:
    # 변수 정의
    end_idx = min(2*K-N, 100000) # K + (K - N)
    dists = [-1 for _ in range(end_idx + 1)]
    # BFS
    print(bfs(N))

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 2*N, N-1, N+1을 for문으로 돌면서, 만약 순간이동을 하는 경우에 queue에 appendleft!!!
# https://fre2-dom.tistory.com/481
# ---------------------------------------------------
import sys
from collections import deque

# 0 - 1 bfs 탐색
def bfs():
    graph = [-1] * 100001
    graph[n] = 0
    queue = deque([n])

    while queue:
        target = queue.popleft()

        # 동생의 위치에 도달했다면 리턴
        if target == k:
            return graph[target]

        # 반복문을 통해 3가지 이동의 경우를 확인
        for i in (target + 1, target - 1, target * 2):

            # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
            if 0 <= i <= 100000 and graph[i] == -1:
                # 순간이동이라면
                if i == target * 2:
                    graph[i] = graph[target] # 0초 갱신
                    queue.appendleft(i) # 순간이동이기에 먼저 탐색

                else:
                    graph[i] = graph[target] + 1
                    queue.append(i)


n, k = map(int, sys.stdin.readline().split())
print(bfs())
"""

"""
# ---------------------------------------------------
# 나의 과거 풀이 -> 순간이동을 굳이 while문을 돌려서 한번에 할 필요 없음. 2*N, N-1, N+1을 for문으로 돌면서, 만약 순간이동을 하는 경우에 queue에 appendleft를 하면됨!!!
# ---------------------------------------------------
from collections import deque

N, K = map(int, input().split())

def bfs(N):
    queue = deque([[N, 0]])
    dists[N] = 0
    while queue:
        N, dist = queue.popleft()
        # 순간이동
        while N <= 2*K-N // 2:
            N = N * 2
            if N == K:
                return dist
            if dists[N] == -1:
                dists[N] = dist
                if 1 <= N - 1 and dists[N - 1] == -1:
                    dists[N] = dist + 1
                    queue.append([N - 1, dist + 1])
                if N + 1 <= 2*K-N and dists[N + 1] == 1:
                    dists[N] = dist + 1
                    queue.append([N + 1, dist + 1])
                if N - 1 == K or N + 1 == K:
                    return dist + 1

if K <= N:
    print(N-K)
else:
    # 변수 정의
    start_idx = max(2*N-K, 0) # N - (K - N)
    end_idx = min(2*K-N, 100000) # K + (K - N)
    dists = [-1 for _ in range(end_idx + 1)]
    # BFS
    result = bfs(N)
    print(result)
"""

"""
N, K = map(int, input().split())
search_start = max(1, 2 * N - K)
search_end = min(100000, 2 * K - N)
# print(dist)

if K <= N:
    print(N - K)
else:
    dists = [abs(k - N) for k in range(search_end + 1)]  # (2*K-N)//2가 아니라, (2*K-N)을 해야함!!!
    for idx in range(search_start, search_end//2 + 1):
        now_idx = idx
        while now_idx <= search_end//2:
            # print(now_idx, (2*K-N)//2)
            dists[now_idx * 2] = min(dists[now_idx * 2], dists[now_idx])
            now_idx = now_idx * 2
        # print("idxes : ", [temp for temp in range((2 * K - N) + 1)])
        # print("dists : ", dists)
    count = 1
    while count < dists[K]:
        if search_start <= (K - count):
            dists[K] = min(dists[K], dists[K - count] + count) # N - count가 아니라, K - count임!!!
        if (K + count) <= search_end:
            dists[K] = min(dists[K], dists[K + count] + count)
        count += 1
    print(dists[K])
"""