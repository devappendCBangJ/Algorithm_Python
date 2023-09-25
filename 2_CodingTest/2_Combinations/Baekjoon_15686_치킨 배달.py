# 80min 소요

from collections import deque

N, M = list(map(int, input().split()))
board = []
houses = []
chicken_houses = []
for r in range(N):
    board.append([])
    input_list = list(map(int, input().split()))
    for c in range(N):
        input_val = input_list[c]
        board[r].append(input_val)
        if input_val == 1:
            houses.append([r, c])
        elif input_val == 2:
            chicken_houses.append([r, c])

# 치킨집 조합 # 삼성 코딩테스트에서는 itertools를 사용할 수 없으므로 직접 구현!!!
chicken_houses_comp = []
for m in range(len(chicken_houses)+1-M):
    queue = deque([[m]])
    while queue:
        val_list = queue.popleft()
        if len(val_list) == M:
            chicken_houses_comp.append(val_list)
        for i in range(val_list[-1]+1, len(chicken_houses)):
            temp_val_list = val_list + [i]
            if M <= len(temp_val_list) + (len(chicken_houses) - (temp_val_list[-1]+1)):
                queue.append(temp_val_list)
                # print(temp_val_list)
# print(chicken_houses_comp)

# 각 집에서 치킨집 사이의 거리 + 그 중에서 최소값 구하기
min_total_distance = 1000000000
for chicken_houses_idx in chicken_houses_comp:
    new_chicken_houses = [chicken_houses[chicken_house_idx] for chicken_house_idx in chicken_houses_idx]
    # print(new_chicken_houses)
    min_house_distance = 0
    for hr, hc in houses:
        min_house_distance += min([abs(hr - chr) + abs(hc - chc) for chr, chc in new_chicken_houses])
    min_total_distance = min(min_total_distance, min_house_distance)
print(min_total_distance)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 거의 완전히 똑같음 but itertools 사용 유무 차이 있음
# https://codesyun.tistory.com/185
# ---------------------------------------------------
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
"""