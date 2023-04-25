# ---------------------------------------------------
# 나의 풀이 -> 특이 케이스 고려하지 못함
# ---------------------------------------------------
"""
# 입력 받기
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# 변수 초기화
station = "ICN"
track = [station]

# Dictionary 생성
tickets_dic = dict()
used_dic = dict()
for t in tickets:
    if t[0] in tickets_dic:
        tickets_dic[t[0]].append(t[1])
        used_dic[t[0]].append(0)
    else:
        tickets_dic[t[0]] = [t[1]]
        used_dic[t[0]] = [0]
# print(tickets_dic, used_dic)

# Dictionary 정렬
for t in tickets_dic.values(): # .values : 실제 dictionary의 value값을 그대로 가져오는 것. 값을 변화시키면 실제값이 변화함!!!
    t.sort()
# print(tickets_dic, used_dic)

# 다음 Station 결정 + 방문 표시 + 경로 저장
for _ in range(len(tickets)):
    for i in range(len(tickets_dic[station])):
        # print(used_dic, station, len(tickets_dic[station]), i)
        if used_dic[station][i] != 1:
            used_dic[station][i] = 1 # 아래 코드와 순서가 바뀌면 안된다!!! 순서 주의!!!
            station = tickets_dic[station][i]
            track.append(station)
            break

# 결과 출력
print(track)
"""

# ---------------------------------------------------
# 나의 풀이 -> BFS로 풀이 불가능한듯?
# ---------------------------------------------------
"""
from collections import deque

# 입력 받기
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# 변수 초기화
queue = deque([["ICN"], ["ICN"]])

# Dictionary 생성
tickets_dic = dict()
used_dic = dict()
for t in tickets:
    if t[0] in tickets_dic:
        tickets_dic[t[0]].append(t[1])
        used_dic[t[0]].append(0)
    else:
        tickets_dic[t[0]] = [t[1]]
        used_dic[t[0]] = [0]

# 다음 Station 결정 + 방문 표시 + 경로 저장
while queue:
    station, track = queue.popleft()
    for i in range(len(tickets_dic[station])):
        # print(used_dic, station, len(tickets_dic[station]), i)
        if used_dic[station][i] != 1:
            used_dic[station][i] = 1 # 아래 코드와 순서가 바뀌면 안된다!!! 순서 주의!!!
            station = tickets_dic[station][i]
            track.append(station)
            break

# 결과 출력
print(track)
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> DFS!!! defaultdict 사용!!! stack 사용!!! stack의 pop을 활용해서 시간복잡도 감소 & 공간 절약!!!
# https://osnim.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89-%EA%B2%BD%EB%A1%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://hi0seon.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS
# https://velog.io/@inhwa1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS
# ---------------------------------------------------
"""
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"], ["ATL", "KOR"]]

from collections import defaultdict

def solution(tickets):
    answer = []
    path = defaultdict(list)
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])
    for key in path.keys():
        path[key].sort(reverse=True) # stack에서 pop하면 오른쪽부터 빠져나가기 때문에, Dictionary를 역순으로 정렬!!!
    print(path)
    stack = ["ICN"]
    while stack:
        top = stack[-1] # stack의 가장 위에 있는 원소 복사!!!
        if not path[top]: # Dictionary에서 다음 경로 존재하지 않는 경우 (다음 경로가 존재하지 않는다는 것 = 경로의 마지막에 있는 원소라는 것)!!!
            answer.append(stack.pop()) # stack에서 가장 오른쪽에 있는 원소 빼서 answer list에 넣음!!!
        else: # Dictionary에서 다음 경로 존재하는 경우!!!
            stack.append(path[top].pop()) # Dictionary의 value에서 가장 오른쪽에 있는 원소 빼서 stack에 넣음!!!
    print(stack)
    answer.reverse() # answer list 순서 뒤집기!!!
    return answer
    
print(solution(tickets))
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> DFS!!! defaultdict 사용!!!
# ---------------------------------------------------
"""
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"], ["ATL", "KOR"]]

from collections import defaultdict

def dfs(graph, N, key, footprint): # DFS는 여러가지 정보 함께 보관!!! 경로 저장도 가능!!!
    print(footprint)

    if len(footprint) == N + 1: # 경로 완성시 결과 return!!!
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx) # graph에서 해당 key의 idx번째에 있는 country 뺀 후, DFS 돌리기!!!

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country) # DFS 돌고 나면, graph에서 해당 key의 idx번째에 있던 country 복구!!!

        if ret: # 경로 완성되었으면 완성된 결과만 return!!!
            print("ret : ", ret)
            return ret

def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

print(solution(tickets))
"""