# ---------------------------------------------------
# 나의 풀이 [35min]
# ---------------------------------------------------
from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

# print(list(combinations(range(N), N//2)))

team_sum_list = []
comb_all = list(combinations(range(N), N//2))
for comb_idx in range(len(comb_all) // 2):
    team_sum1, team_sum2 = 0, 0
    team_sum1 = sum([S[s[0]][s[1]] + S[s[1]][s[0]] for s in list(combinations(comb_all[comb_idx], 2))])
    team_sum2 = sum([S[s[0]][s[1]] + S[s[1]][s[0]] for s in list(combinations(comb_all[-(comb_idx+1)], 2))]) # +1 필수!!!
    team_sum_list.append(abs(team_sum2 - team_sum1))
    # print(team_sum_list)
print(min(team_sum_list))