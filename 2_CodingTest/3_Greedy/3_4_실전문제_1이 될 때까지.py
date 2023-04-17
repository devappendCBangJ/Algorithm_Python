# # 입력 받기
# N, K = list(map(int, input().split()))
#
# # count 세기
# count = 0
# while N > 1: # 조건 주의!!!
#     _, r = divmod(N, K)
#     if r == 0:
#         N //= K
#     else:
#         N -= 1
#     count += 1
#
# # 결과 출력
# print(count)

# ---------------------------------------------------
# 교재 풀이 -> 점화식 -> 시간복잡도 효율적
# ---------------------------------------------------
"""
# 입력 받기
N, K = list(map(int, input().split()))

# count 세기
result = 0
while N > K:
    # N에서 얼만큼 빼야 K로 나눌수 있을까? -> 점화식으로 표현 -> 연산량 감소 !!!
    r = (N % K)
    result += r
    N -= r
    # K로 나눌 수 있는 경우 !!!
    N //= K
    result += 1
# 최종 count !!!
result += (N - 1)

# 결과 출력
print(result)
"""