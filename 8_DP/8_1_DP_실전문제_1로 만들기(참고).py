# input
x = int(input())

# DP table 초기화
d = [0] * 30001

# DP 수행
for i in range(2, x+1):
    # 현재값 - 1
    d[i] = d[i-1] + 1
    # 현재값이 2로 나누어 떨어짐
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재값이 3으로 나누어 떨어짐
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재값이 5로 나누어 떨어짐
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

# 결과 출력
print(d[x])