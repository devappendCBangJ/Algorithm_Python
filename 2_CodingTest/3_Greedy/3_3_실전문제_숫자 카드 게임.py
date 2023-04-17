# 입력 받기
N, M = list(map(int, input().split()))

# 각 행의 최소값들 중에서 최대값 추출
max_val = 0
for _ in range(N):
    row_min_val = min(list(map(int, input().split())))
    if row_min_val > max_val:
        max_val = row_min_val

# 결과 출력
print(max_val)

# ---------------------------------------------------
# 교재 풀이 -> 나와 유사
# ---------------------------------------------------
"""
# 입력 받기
N, M = list(map(int, input().split()))

# 각 행의 최소값들 중에서 최대값 추출
result = 0
for _ in range(N):
    data = list(map(int, input().split()))
    row_min_val = min(data)
    result = max(result, row_min_val)

# 결과 출력
print(result)
"""

# ---------------------------------------------------
# 교재 풀이 -> 이중 for문 비효율적
# ---------------------------------------------------
"""
# 입력 받기
N, M = list(map(int, input().split()))

# 각 행의 최소값들 중에서 최대값 추출
result = 0
for _ in range(N):
    data = list(map(int, input().split()))
    row_min_val = 10001
    for d in data:
        row_min_val = min(row_min_val, d)
    result = max(result, row_min_val)

# 결과 출력
print(result)
"""