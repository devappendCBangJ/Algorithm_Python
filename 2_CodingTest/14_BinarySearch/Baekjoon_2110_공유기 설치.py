N, C = list(map(int, input().split()))
houses = [int(input()) for _ in range(N)]
houses.sort()

# 공유기 사이의 거리를 이분탐색!!!
start = 1
end = houses[-1] - houses[0]
while start <= end: # 시간복잡도 : logn (이분탐색) * n (설치 가능 공유기 개수 count)!!!
    current = houses[0]
    mid = (start + end) // 2 # 13번 line에서의 이유로, current와 mid 변수를 따로 관리해야함!!!
    count = 1
    for idx in range(1, len(houses)):
        if mid <= houses[idx] - current: # houses[idx] - houses[idx-1]로 하면 안됨. houses[idx] - current로 하고, mid보다 이 값이 커졌을 때 current를 다시 업데이트 해야함!!!
            current = houses[idx]
            count += 1
    if C <= count:
        start = (start + end) // 2 + 1
        result = mid # 다음 while문에서 여기 if문을 못들어올 수 있으므로, C <= count를 성공했을 때 무조건 result 변수에 기억해두어야함!!!
    else:
        end = (start + end) // 2 - 1
print(result)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 공유기 사이의 거리를 이분탐색함!!!
# https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-2110-%EA%B3%B5%EC%9C%A0%EA%B8%B0-%EC%84%A4%EC%B9%98-Python
# ---------------------------------------------------
N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start = 1 # 공유기 거리 최소
end = arr[-1] - arr[0] # 공유기 거리 최대
result = 0

# 재귀로 적절한 두 공유기 사이의 거리를 찾는다
while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 거리
    current = arr[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(result)
"""