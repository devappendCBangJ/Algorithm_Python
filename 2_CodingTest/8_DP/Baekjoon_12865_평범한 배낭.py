# 120min 소요 실패

N, K = map(int, input().split())

dp_table = [0 for _ in range(K + 1)]
for _ in range(N):
    W, V = map(int, input().split())
    for idx in range(K, W - 1, -1): # 뒤에서부터 업데이트 하지 않으면, 이전에 할당한 값이 이후 값에 영향을 줌!!!
        if 0 <= idx - W:
            dp_table[idx] = max(dp_table[idx - W] + V, dp_table[idx])
    print(dp_table)
print(dp_table[-1])

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 1차원 DP 활용 + items에 대한 for문을 가장 바깥으로 뺌!!!
# https://codingmovie.tistory.com/48
# ---------------------------------------------------
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
dp = [0 for _ in range(K + 1)]
for item in items: # items에 대한 for문을 가장 바깥으로 빼서, 중복해서 같은 item을 사용하는 경우 방지!!!
    w, v = item
    for i in range(K,w-1,-1): # DP Table을 2차원이 아닌, 1차원으로 만들기 위한 방법!!!
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])
"""

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 2차원 DP 활용 + items에 대한 for문을 가장 바깥으로 뺌!!!
# https://velog.io/@highcho/Algorithm-baekjoon-12865
# ---------------------------------------------------
import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(n): # items에 대한 for문을 가장 바깥으로 빼서, 중복해서 같은 item을 사용하는 경우 방지!!!
	w, v = map(int, sys.stdin.readline().split())
	for j in range(1, k + 1): # DP Table을 굳이 2차원으로 만들 필요 없이 덮어씌우면 됨. 이전값을 다시 쓸 상황이 없는데 굳이 기억해서 공간복잡도만 더 잡아먹음!!!
		if j >= w:
			dp[i + 1][j] = max(dp[i][j - w] + v, dp[i][j])
		else:
			dp[i + 1][j] = dp[i][j]
print(dp[n][k])
"""

"""
# ---------------------------------------------------
# 나의 과거 풀이 -> 1차원 DP 활용. items for문을 가장 바깥으로 빼면, 공간복잡도 훨씬 개선될 듯!!! 분석해봐도 이 코드가 왜 안되는지는 모르겠음!!!
# https://velog.io/@highcho/Algorithm-baekjoon-12865
# ---------------------------------------------------
N, K = map(int, input().split())

# DP Table 초기화
dp_table = [[0, set()] for _ in range(K + 1)]
things = []
idx = 0
for n in range(N):
    W, V = map(int, input().split())
    if W <= K:
        things.append([W, V])
        dp_table[W][0] = V
        dp_table[W][1].add(idx)
        idx += 1
print(dp_table)

# DP Table 업데이트
for k in range(0, K): # weight이 0인 물건이 존재하기 때문에, idx가 0인 지점부터 고려해줘야함!!!
    for idx, (w, v) in enumerate(things):
        if idx not in dp_table[k][1] and k + w <= K:
            if dp_table[k][0] + v >= dp_table[k + w][0]:
                dp_table[k + w][0] = dp_table[k][0] + v
                dp_table[k + w][1] = dp_table[k][1].copy() # 이렇게 하면 주소가 복사되는데, 이전의 값은 어차피 더는 사용하지 않기 때문에 이렇게 해도 문제 푸는데 지장은 없음!!!
                dp_table[k + w][1].add(idx) # dp_table에서 새로운 idx까지 사용한 물건도 저장해둬야함. 이전 사용했던 물건들에서 현재 방문한 물건을 추가시킨 것을 새로운 idx위치에 넣어주면 됨!!!
    if dp_table[k + 1][0] <= dp_table[k][0]: # 다음 value가 더 작거나 같으면, 현재 정보로 다음 DP Table을 업데이트 (다음 value와 현재 value가 같은 경우, 이전이 더 작은 weight로 같은 value를 뽑아낸 것이기 때문에 weight을 아끼기 위해 이렇게 함)!!!
        dp_table[k + 1] = dp_table[k].copy()

# 최종 결과 출력
print(dp_table)
print(dp_table[K][0])
"""