progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))

def solution(progresses, speeds):
    i = 0
    answer = []
    while i < len(progresses):
        count = 0
        day_mul = ((100 - progresses[i]) // speeds[i]) + 1 if (100 - progresses[i]) // speeds[i] != int((100 - progresses[i]) // speeds[i]) else (100 - progresses[i]) // speeds[i]
        for p in range(i, len(progresses)): # 점화식!!!
            progresses[p] = min(progresses[p]+(speeds[p]*day_mul), 100)
        while progresses[i] == 100:
            i += 1
            count += 1
            if i >= len(progresses): # 조건문 경우 생각!!!
                break
        answer.append(count)
    return answer

print(solution(progresses, speeds))