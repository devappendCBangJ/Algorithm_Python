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
        quick_sort(buckets_list[k])
        final_list = final_list + buckets_list[k]
    return final_list

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
        arr[low], arr[m] = arr[m], arr[low] # pivot 위치로 swap o
        return m

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