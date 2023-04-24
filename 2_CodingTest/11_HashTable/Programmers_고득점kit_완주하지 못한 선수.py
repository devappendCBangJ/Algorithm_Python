participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

# participant = input().split()
# completion = input().split()
#
# for c in completion:
#     participant.remove(c)
# print(participant[0])

part_dic = dict()
comp_dic = dict()
for p in participant:
    if p in part_dic:
        part_dic[p] += 1
    else:
        part_dic[p] = 1
for c in completion:
    if c in comp_dic:
        comp_dic[c] += 1
    else:
        comp_dic[c] = 1
for k in part_dic.keys():
    if k not in comp_dic:
        print(k)
    elif part_dic[k] != comp_dic[k]:
        print(k)

# ---------------------------------------------------
# 다른 사람 풀이 -> collections.Counter 활용!!!
# ---------------------------------------------------
"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> hash 활용!!!
# ---------------------------------------------------
"""
def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> 정렬 후, completion에 없는 participant의 원소 출력
# ---------------------------------------------------
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1] # participant의 마지막 원소가 completion에 없는 경우!!!
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> 정렬 후, completion에 없는 participant의 원소 출력
# ---------------------------------------------------
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
"""