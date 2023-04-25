# n = 3
# lost = [3]
# reserve = [1]

n = input()
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

count = 0
n_list = [1 for _ in range(n)]

for l in lost:
    n_list[l-1] -= 1
for r in reserve:
    n_list[r-1] += 1
for i in range(n):
    if i == 0:
        if n_list[i] == 0:
            if n_list[i+1] == 2:
                n_list[i+1] = 1
                n_list[i] = 1
    elif i == n-1:
        if n_list[i] == 0:
            if n_list[i-1] == 2:
                n_list[i-1] = 1
                n_list[i] = 1
    else:
        if n_list[i] == 0:
            if n_list[i-1] == 2:
                n_list[i-1] = 1
                n_list[i] = 1
            elif n_list[i+1] == 2:
                n_list[i+1] = 1
                n_list[i] = 1
for n in n_list:
    if n >= 1:
        count += 1
print(count)

# ---------------------------------------------------
# 다른 사람 풀이
# ---------------------------------------------------
"""
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
"""