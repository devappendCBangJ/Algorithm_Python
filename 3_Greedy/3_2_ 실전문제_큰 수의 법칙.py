# 입력 받기
N, M, K = map(int, input().split())
N_list = sorted(map(int, input().split()), reverse=True)

# 제일 큰놈 or 두번재로 큰놈 더함
count = 0
result = 0
for _ in range(M):
    if count < K:
        result += N_list[0]
    else:
        result += N_list[1]
        count = -1
    count += 1

# 결과 출력
print(result)

# ---------------------------------------------------
# 교재 풀이 -> 점화식 -> 시간복잡도 효율적
# ---------------------------------------------------
"""
# 입력 받기
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# 정렬, 값 할당
data.sort()
first, second = data[N-1], data[N-2]

# 가장 큰 수의 개수
max_count = int(M / (K+1)) * first + M % (K+1) # 점화식 세울 수 있음!!!

# 최종값
result = 0
result += max_count * first
result += (M - max_count) * second

print(result)
"""