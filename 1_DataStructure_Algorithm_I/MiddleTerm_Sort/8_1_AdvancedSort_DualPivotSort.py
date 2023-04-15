import time

def DualPivotQuick_sort(arr, low, high):
    if low < high:
        lp, rp = partition(arr, low, high)

        DualPivotQuick_sort(arr, low, lp - 1)
        DualPivotQuick_sort(arr, lp + 1, rp - 1)
        DualPivotQuick_sort(arr, rp + 1, high)

def partition(arr, low, high):
    # pivot1, pivot2, curr, left, right 지정
    if arr[low] > arr[high]:        # low 값 = pivot1 값, high 값 = pivot2 값로 지정하려고 하는데 pivot1이 pivot2보다 작아지도록 만듦
        arr[low], arr[high] = arr[high], arr[low]

    left = curr = low + 1           # low 값 = pivot1 값, high 값 = pivot2 값이므로, low + 1, high - 1부터 시작
    right, pivot1, pivot2 = high - 1, arr[low], arr[high]

    # low + 1 ~ high - 1까지 반복
    while curr <= right:            # curr 인덱스가 right 인덱스보다 작거나 같은 경우
        # curr 값 < pivot1 값 : curr을 왼쪽 영역에 넣음
        if arr[curr] < pivot1:      # curr 값이 pivot1 값보다 작은 경우
            arr[curr], arr[left] = arr[left], arr[curr]     # curr 값과 left 값 swap
            left += 1               # left 인덱스 증가

        # curr 값 > pivot2 값
            # right 값 > pivot2 값 & curr 인덱스 < right 인덱스 : right를 오른쪽 영역에 넣음
            # 무조건 : curr을 오른쪽 영역에 넣음
            # curr 값(직전 코드에서 right 값과 curr 값을 스왑했으므로 원래는 right 값이었음) < pivot1 값 : curr을 왼쪽 영역에 넣음
        elif arr[curr] >= pivot2:   # curr 값이 pivot2 값보다 크거나 같은 경우
            while arr[right] > pivot2 and curr < right:     # right 값이 pivot2보다 크고, left가 right보다 작은 경우
                right -= 1          # right 인덱스 감소

            arr[curr], arr[right] = arr[right], arr[curr]   # curr 값과 right 값 swap
            right -= 1              # right 인덱스 감소
            
            # 아래서 curr을 1개 증가시켜서 다시 오지 않을 것이므로 이 작업도 필수
            if arr[curr] < pivot1:  # curr 값이 pivot1 값보다 작은 경우
                arr[curr], arr[left] = arr[left], arr[curr] # curr 값과 left 값 swap
                left += 1           # left 인덱스 증가
        curr += 1                   # curr 인덱스 증가

    # left, right 원위치 : while문을 다시 돌리려고 left -= 1, right += 1했는데 while 다시 안돌아서 내려온 것이므로 원위치 시켜줌
    left -= 1                       # left 인덱스 감소
    right += 1                      # right 인덱스 증가

    # pivot1, pivot2 본래 위치로 swap
    arr[low], arr[left] = arr[left], arr[low]               # low 값과 left 값 swap
    arr[high], arr[right] = arr[right], arr[high]           # high 값과 right 값 swap

    # pivot1, pivot2 인덱스 반환
    return left, right

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
    DualPivotQuick_sort(arr, 0, 1000)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산
# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")
