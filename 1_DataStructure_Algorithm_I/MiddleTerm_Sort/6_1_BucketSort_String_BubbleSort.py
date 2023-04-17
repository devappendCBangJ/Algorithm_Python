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
        bubble_sort(buckets_list[k])
        final_list = final_list + buckets_list[k]
    return final_list

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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