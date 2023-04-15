import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if (arr[j] < arr[i - 1]):
                t = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = t
            else:
                break
            i = i - 1
    return arr

def merge(arr1, arr2):
    a = 0
    b = 0
    temp = []

    while(a < len(arr1) and b < len(arr2)):
        if(arr1[a] < arr2[b]):
            temp.append(arr1[a])
            a = a + 1
        elif(arr1[a] > arr2[b]):
            temp.append(arr2[b])
            b = b + 1
        else:
            temp.append(arr1[a])
            temp.append(arr2[b])
            a = a + 1
            b = b + 1
    while(a < len(arr1)):
        temp.append(arr1[a])
        a = a + 1
    while(b < len(arr2)):
        temp.append(arr2[b])
        b = b + 1

    return temp

def tim_sort(arr):
    for x in range(0, len(arr), run):
        arr[x : x + run] = insertion_sort(arr[x : x + run])
    runinc = run
    while(runinc < len(arr)):
        for x in range(0, len(arr), 2 * runinc):
            arr[x : x + 2 * runinc] = merge(arr[x : x + runinc], arr[x + runinc : x + 2 * runinc])
        runinc = runinc * 2

# arr = [3, 30, 23, 35, 8, 10, 40, 55, 50, 52]
# run = 5
# tim_sort()
# print(arr)

# Average Filter : 실행 시간 계속 달라지므로 여러번 반복하여 평균 취함
tot_time = [0] * 1001
repeat = 5
min_time = 10000.0
max_time = 0.0
min_idx = 0
max_idx = 0
for i in range(1, 1001):
    run = i
    for j in range(repeat):
        arr = []
        # 메모장 열기
        with open('name.txt', 'r') as file:
            line = None
            # 1줄씩 읽고 배열에 넣기
            while line != '':
                line = file.readline()
                arr.append(line.strip('\n'))
        # 시간 측정
        start = time.time_ns()
        tim_sort(arr)
        end = time.time_ns()
        tot_time[i] += (end - start)
    tot_time[i] = tot_time[i] / 1000000000 / repeat  # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산
    if min_time > tot_time[i]:
        min_time = tot_time[i]
        min_idx = i
    if max_time < tot_time[i]:
        max_time = tot_time[i]
        max_idx = i

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(1, 1001):
    print(f"run[{i}] {tot_time[i]:.7f} sec")
print("min : ", min_time)
print("min idx : ", min_idx)
print("max : ", max_time)
print("max idx : ", max_idx)
