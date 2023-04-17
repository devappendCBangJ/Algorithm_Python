import time

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
        temp = [0] * 1001 # 임시 배열
        n = high - low + 1 # 배열 원소 개수
        left, right = low, mid + 1
        k = 0

        while left <= mid and right <= high: # 배열 절반 쪼갬. 두 배열끼리 첫번째 인덱스부터 비교. 작은 것을 임시배열에 담음
            if arr[left] <= arr[right]:
                temp[k] = arr[left]
                left += 1
            else:
                temp[k] = arr[right]
                right += 1
            k += 1

        while left <= mid: # 두 배열 중 한 배열이 남으면 전부 순서대로 임시배열에 담음
            temp[k] = arr[left]
            left += 1
            k += 1
        while right <= high:
            temp[k] = arr[right]
            right += 1
            k += 1

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
    merge_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")