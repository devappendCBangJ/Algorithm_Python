# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

# 입력 받기
num = int(input())
sizes = []
for _ in range(num):
    sizes.append(list(map(int, input().split())))
# print(sizes)

# 변수 초기화
max_w, max_h = 0, 0

# 지갑 최소값 구하기
for idx, size in enumerate(sizes): # list에서 for문으로 하나씩 원소 뽑아오면, 실제 배열 원소의 주소를 가져온 것!!!
    if size[1] > size[0]:
        size[0], size[1] = size[1], size[0]
    if size[0] > max_w:
        max_w = size[0]
    if size[1] > max_h:
        max_h = size[1]
print(max_w * max_h)

# ---------------------------------------------------
# 다른 사람 풀이 -> 큰 것 중에 큰 것, 작은 것 중에 큰 것!!!
# ---------------------------------------------------
"""
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> 정렬 후, 큰 것 중에 큰 것, 작은 것 중에 큰 것!!!
# ---------------------------------------------------
"""
def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    return max([x[0] for x in sizes]) * max([x[1] for x in sizes])
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> 나와 유사
# ---------------------------------------------------
"""
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
"""