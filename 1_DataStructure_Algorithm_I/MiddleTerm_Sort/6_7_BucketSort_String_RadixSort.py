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
        if (len(buckets_list[k]) != 0):
            buckets_list[k] = radix_sort(buckets_list[k])
            final_list = final_list + buckets_list[k]
    return final_list

def sort(array, size, col, base):
    # output : sorting된 원소 담는 배열
    output = [0] * size
    # count : 문자 개수 배열
    count = [0] * (base + 1)

    min_base = ord('A') - 1 # string이 나타낼 수 있는 아스키코드 최소값
    # count : 문자 개수 계산
    for item in array:
        letter = ord(item[col]) - min_base if col < len(item) else 0 # 현재 원소 길이 > 확인하고 싶은 문자열 인덱스 : 숫자 개수 count++, 현재 원소 길이 < 확인하고 싶은 문자열 인덱스 : 숫자 개수 0
        count[letter] += 1

    # count : 문자 개수 누적합 계산 -> output 배열에 sorting할 때, 해당 숫자가 어느 위치에 들어가야할지 파악 가능. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
    for i in range(len(count)-1):
        count[i + 1] += count[i]

    # B : sorting된 원소 담음. C가 B의 인덱스를 알려줌
    for item in reversed(array):
        letter = ord(item[col]) - min_base if col < len(item) else 0 # 현재 원소 길이 > 확인하고 싶은 문자열 인덱스 : 숫자 개수 count++, 현재 원소 길이 < 확인하고 싶은 문자열 인덱스 : 숫자 개수 0
        output[count[letter] - 1] = item # output 배열의 인덱스 0번부터 값을 넣기 위해. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
        count[letter] -= 1 # 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦

    return output

def radix_sort(array, max_count = None):
    # 길이가 가장 긴 문자열 반환
    if not max_count:
        max_count = len(max(array, key = len)) # max(array, key = len) : string의 관점에서 배열에서 최대값을 갖는 원소 추출

    # 각 원소의 마지막 문자 -> 각 원소의 처음 문자 순으로 비교 + 정렬
    for cnt in range(max_count-1, -1, -1): # max_len-1, max_len-2, ...0
        array = sort(array, len(array), cnt, 67) # 67 : 아스키코드 A~z까지 문자 개수
    return array

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