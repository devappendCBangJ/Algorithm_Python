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
        merge_sort(buckets_list[k])
        final_list = final_list + buckets_list[k]
    return final_list

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