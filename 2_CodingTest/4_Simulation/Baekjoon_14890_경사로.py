# 120min 소요

N, L = list(map(int, input().split()))
board = []
for n in range(N):
    board.append(list(map(int, input().split())))

def is_parallel(line):
    pre_val = line[0]
    pre_count = 1
    debt = 0
    for i in range(1, N):
        if pre_val == line[i]:
            pre_count += 1
            if 0 < debt:
                debt -= 1
                if debt == 0: # 빚을 전부 갚은 경우, count를 0으로 바꿔줘야 그 이후 시점부터 다시 셀 수 있음!!!
                    pre_count = 0
        else:
            if 0 < debt:
                return 0
            if pre_val == line[i] - 1 and pre_count < L:
                return 0
            elif pre_val == line[i] + 1:
                debt = L - 1
                if debt == 0: # L이 1인 경우, 처음부터 현재 시점부터 빚을 갚은 것이 되어버림. 빚을 갚은 순간 count가 0이 되어야하므로 이 부분 추가!!!
                    pre_count = 0
            elif 2 <= abs(pre_val - line[i]): # 2 이상 차이나는 경우를 빠뜨림!!!
                return 0
            else:
                pre_count = 1
            pre_val = line[i]
    if debt == 0: # for문 다 돌아도, debt가 0이 아닌 경우에는 만족이 되지 않음!!!
        return 1
    else:
        return 0

result = 0
for n in range(N):
    line = board[n]
    if is_parallel(line) == 1:
        # print(n)
        result += 1
    line = [board[r][n] for r in range(N)]
    if is_parallel(line) == 1:
        # print(line, n)
        result += 1
print(result)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> line[i] > line[i-1]인 경우 다시 앞으로 돌아가므로, 조금 더 비효율적. 대신 조금 더 간단
# https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-14890-%EA%B2%BD%EC%82%AC%EB%A1%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# ---------------------------------------------------
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def check_line(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or slope[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True


for i in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for i in range(n)]):
        ans += 1

print(ans)
"""