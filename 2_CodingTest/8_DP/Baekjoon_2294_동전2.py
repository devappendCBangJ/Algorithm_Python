# 30min 소요

n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]
dp = [1000000000 for _ in range(k+1)]
dp[0] = 0

for val, count in enumerate(dp):
    # print(dp)
    if count == 1000000000:
        continue
    for coin in coins:
        new_val = val + coin
        if new_val <= k:
            dp[new_val] = min(dp[val] + 1, dp[new_val])
print(-1 if dp[-1] == 1000000000 else dp[-1])

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> dp부터 돌리는 것이 아니라, coin부터 돌림. 문제에서의 결과는 나와 다른 사람의 풀이가 같음
# 이 풀이는 coin을 전부 돌고 나서야 최적의 dp가 완성됨. 나의 풀이는 dp에서 idx를 하나 돌때마다 이전의 값들은 항상 최적의 값임
# https://sodehdt-ldkt.tistory.com/75
# ---------------------------------------------------
n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
    
dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for i in range(c,k+1):
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])
"""