import time

def bucket_sort(arr):
    # bucket list의 size 범위 설정
    size = 26

    # input list와 크기가 같은 2차원 bucket list 생성(bucket의 크기를 input list의 크기와 같은 것을 사용하겠다!)
    buckets_list = []
    for i in range(size):
        buckets_list.append([]) # [[], [], [], [], []]꼴 2차원 배열 생성
    # print(buckets_list) # 확인용 코드

    # 해당 bucket list에 input list의 원소 분류
    for j in range(len(arr)-1): # 메모장 파일 열어서 불러올때, 배열의 마지막 인덱스에 \n이 추가로 들어가서 1000개가 아닌 1001개가 되어버리므로 len(input_list)-1번을 돌아서 의미없는 문자는 세지 않음
        # print(input_list[i]) # 확인용 코드
        # print(arr[i][0]) # 확인용 코드
        # print(ord(input_list[i][0])) # 확인용 코드
        k = (ord(arr[j][0]) - 65) % size
        buckets_list[k].append(arr[j])
        # print(buckets_list) # 확인용 코드

    # bucket list별로 정렬 + 결과 합치기
    final_list = []
    for k in range(len(buckets_list)):
        DualPivotQuick_sort(buckets_list[k],0,len(buckets_list[k])-1)
        final_list = final_list + buckets_list[k]
    return final_list

def DualPivotQuick_sort(arr, low, high):
    if low < high:
        lp, rp = partition(arr, low, high)

        DualPivotQuick_sort(arr, low, lp - 1)
        DualPivotQuick_sort(arr, lp + 1, rp - 1)
        DualPivotQuick_sort(arr, rp + 1, high)

def partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]

    while k <= g:
        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1

        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1

            arr[k], arr[g] = arr[g], arr[k]
            g -= 1

            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1
        k += 1
    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]

    return j, g

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while (0 < j) and (arr[j] < arr[j - 1]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    def sort(low, high):
        if(low < high): # low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
            # pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류. reculsive하게 반복(pivot 자체는 sorting에 참여 x)
            pivot_idx = partition(low, high)

            # 배열 2등분 reculsive하게 반복
            sort(low, pivot_idx - 1)
            sort(pivot_idx + 1, high)

    def partition(low, high):
        pivot = arr[low] # pivot 선택
        m = low # S1, S2가 비워진 상태에서 시작

        for k in range(low + 1, high + 1): # pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 순회 ♣
            if(arr[k] < pivot): # case2(pivot보다 더 작은 원소인 경우) : swap o, case1(pivot보다 더 큰 원소인 경우) : swap x
                m += 1
                arr[k], arr[m] = arr[m], arr[k]
            else:
                pass
        arr[low], arr[m] = arr[m], arr[low] # pivot 위치로 swap o. 그냥 swap 안하고 바로 return을 low로 줘도 된다
        return m

    return sort(0, len(arr) - 1)

def merge_sort(arr):
    def sort(low, high):
        if low < high: # low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
            # 배열 2등분 reculsive하게 반복
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid + 1, high)

            # 2등분된 배열 조각들끼리 원소들간 비교 + sorting + merge 반복
            merge(low, mid, high)

    def merge(low, mid, high):
        temp = [] # 임시 배열
        n = high - low + 1 # 배열 원소 개수
        left, right = low, mid + 1

        while left <= mid and right <= high: # 배열 절반 쪼갬. 두 배열끼리 첫번째 인덱스부터 비교. 작은 것을 임시배열에 담음
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid: # 두 배열 중 한 배열이 남으면 전부 순서대로 임시배열에 담음
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(n): # 임시 배열 원소를 기존 배열로 붙여넣기
            arr[low + i] = temp[i]

    return sort(0, len(arr) - 1)

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
    arr = bucket_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")