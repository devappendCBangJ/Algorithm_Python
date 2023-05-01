# 라이브러리 불러오기
from collections import deque

# 입력 받기
numbers = list(map(int, (input().split())))
target = int(input())

# 변수 초기화
count = 0
queue = deque()
queue.append([-1, 0])

# BFS
while queue:
    # print(queue)
    idx, result = queue.popleft()
    if idx < len(numbers) - 1:
        queue.append([idx + 1, result + numbers[idx + 1]])
        queue.append([idx + 1, result - numbers[idx + 1]])
    if idx == len(numbers)-1 and result == target:
        count += 1

# 결과 출력
print(count)

# ---------------------------------------------------
# 다른 사람 풀이 -> 데카르트 곱 이용 !!
# ---------------------------------------------------
"""
# 라이브러리 불러오기
from itertools import product

# 입력 받기
numbers = list(map(int, (input().split())))
target = int(input())

# 데카르트 곱
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # print(l)
    # print(*l)
    # print(product(*l))
    # print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)

# 결과 출력
print(solution(numbers, target))
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> Recursion 이용 !!
# ---------------------------------------------------
"""
# 입력 받기
numbers = list(map(int, (input().split())))
target = int(input())

# Recursion
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 결과 출력
print(solution(numbers, target))
"""

# ---------------------------------------------------
# 다른 사람 풀이 -> DFS 이용 !!
# ---------------------------------------------------
"""
# 입력 받기
numbers = list(map(int, (input().split())))
target = int(input())

# DFS
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return
    elif(idx == N):
        return

    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])
    
def solution(numbers, target):
    DFS(0, numbers, target, 0)
    return answer
    
# 결과 출력
print(solution(numbers, target))
"""
# ---------------------------------------------------
# 다른 사람 풀이 -> list 이용 !!
# ---------------------------------------------------
"""
# 입력 받기
numbers = list(map(int, (input().split())))
target = int(input())

# list 활용
def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)

# 결과 출력
print(solution(numbers, target))
"""