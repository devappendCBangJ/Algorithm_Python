import time

def dual_pivot_sort(arr, low, high):
    if high <= low:
        return
    k = low + 1
    h = low + 1
    l = high - 1
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    while k <= l:
    # the last non-check index is l,as l+1 to high - 1 is the part III,
    #where all elements > arr[high]
        pivot1 = arr[low]
        pivot2 = arr[high]
        if arr[k] < pivot1:
            arr[h], arr[k] = arr[k], arr[h]
            #h is the first element of part II
            h += 1
            #increase h by 1, for pointing to the first element of part II
            k += 1
            #increase k by 1, because we have checked arr[k]
        elif arr[k] > pivot2:
        #l is the last element of part IV
            arr[k], arr[l] = arr[l], arr[k]
            #don't increase k, as we have not check arr[l] yet
            l -= 1
            #after swap, we should compare arr[k] with arr[low] and arr[high] again
        else: k += 1
        # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1#now,h is the last element of part I
    l += 1 #now, l is the first element of part III
    arr[low], arr[h] = arr[h], arr[low]
    arr[high], arr[l] = arr[l], arr[high]
    
    # pivot1,2 기준 배열 3등분
    dual_pivot_sort(arr, low, h-1)
    dual_pivot_sort(arr, h+1, l-1)
    dual_pivot_sort(arr, l+1, high)

 # Average Filter : 실행 시간 계속 달라지므로 여러번 반복하여 평균 취함
tot_time = 0
repeat = 500
for i in range(repeat):
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
    dual_pivot_sort(arr, 0, len(arr) - 1)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")