answers = list(map(int, input().split()))

def solution(answers):
    pred1 = [1, 2, 3, 4, 5]
    pred2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pred3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx1, idx2, idx3 = 0, 0, 0
    cnt1, cnt2, cnt3 = 0, 0, 0
    max = -1
    answer = []

    for a in answers:
        if pred1[idx1] == a:
            cnt1 += 1
        if pred2[idx2] == a:
            cnt2 += 1
        if pred3[idx3] == a:
            cnt3 += 1
        idx1 += 1
        if idx1 == len(pred1):
            idx1 = 0
        idx2 += 1
        if idx2 == len(pred2):
            idx2 = 0
        idx3 += 1
        if idx3 == len(pred3):
            idx3 = 0
    for idx, c in enumerate([cnt1, cnt2, cnt3]):
        if c > max:
            max = c
            answer = [idx + 1]
        elif c == max:
            answer.append(idx + 1)
    return answer

print(solution(answers))

# ---------------------------------------------------
# 다른 사람 풀이 -> 가독성 향상 / 공간 복잡도 절약 !
# ---------------------------------------------------
"""
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> 가독성 향상 / 공간 복잡도 절약
# ---------------------------------------------------
"""
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> itertools.cycle 활용 !!
# ---------------------------------------------------
"""
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
"""