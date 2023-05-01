# 라이브러리 불러오기
from collections import deque

# 입력 받기
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# target이 words에 존재?
if target in words:
    queue = deque([[0, begin]])
    while queue:
        level, now = queue.popleft()
        # 이웃 여부 확인 + 이웃이면 queue에 넣기
        for word in words[:]:
            count = 0
            for i in range(len(begin)):
                if now[i] != word[i]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                if word == target:
                    print(level+1)
                else:
                    queue.append([level+1, word])
                    words.remove(word) # remove의 시간복잡도 큼. 차라리 방문 경로를 저장해두는 것이 더 나음 !!
else:
    print(0)

# ---------------------------------------------------
# 다른 사람 풀이 -> 전체적으로 비효율적 / 지난 경로 기억에 dict 사용 !!! zip으로 string 2개를 묶어서 한 번에 풀어냄 !!! 제너레이터 사용 !!!
# ---------------------------------------------------
"""
from collections import deque

def get_adjacent(current, words):
    for word in words:
        count = 0
        for c, w in zip(current, word): # 중간에 count가 1 초과면 break 시키는 것이 더 효율적일듯 / zip으로 할 수도 있구나!!!
            if c != w:
                count += 1

        if count == 1: # 제너레이터 사용!!!
            yield word

def solution(begin, target, words):
    dist = {begin: 0} # 딕셔너리로 할 수도 있구나!!!
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words): # words에서 이미 방문했던 words를 또 다시 불러오는게 비효율적
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0) # !!!
"""
# ---------------------------------------------------
# 다른 사람 풀이 -> dfs풀이 !!! list에서 원소 하나 제거하는 방법 !!!
# ---------------------------------------------------
"""
answer = 0
def solution(begin, target, words):
    dfs(begin, target, 0, words)
    return answer

def change(fr, to):
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]: # 단어에서 1개의 문자를 뺐을 때, 두 단어가 같은가!!
            return True
    return False

def dfs(begin, target, d, words):
    global answer
    if begin == target:
        answer = d
        return
    else:
        if len(words) == 0: # words에 원소가 하나도 없으면 return !!
            return
        for w in range(len(words)):
            if change(begin, words[w]):
                word = words[:w]+words[w+1:] # words에서 이미 방문한 word는 words list에서 제거!!!
                dfs(words[w], target, d+1, word)
"""
# ---------------------------------------------------
# 다른 사람 풀이 -> bfs 신기한 방법 !!!
# ---------------------------------------------------
"""
def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = [] # temp_Q : 다음 탐색할 원소들 저장 / Q : 이번에 탐색할 원소들 !!!
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q: # !!
            return 0
        Q = temp_Q # !!!
        answer += 1
"""