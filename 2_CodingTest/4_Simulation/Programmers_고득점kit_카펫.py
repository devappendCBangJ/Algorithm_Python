brown = 10
yellow = 2

print([int((brown/4)-1 + (((brown/4)-1)**2 - yellow)**0.5 + 2), int((brown/4)-1 - (((brown/4)-1)**2 - yellow)**0.5 + 2)])

# ---------------------------------------------------
# 다른 사람 풀이 -> w 값을 내리면서, h 값을 올리면서 찾아냄
# ---------------------------------------------------
"""
def solution(brown, yellow):
    w = (brown / 2) + 1
    h = 1
    while w >= h:
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
        w -= 1
        h += 1
"""