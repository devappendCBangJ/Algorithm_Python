import time

def sort(array, size, col, base):
    # output : sorting된 원소 담는 배열
    output = [0] * size
    # count : 문자 개수 배열
    count = [0] * (base + 1)

    min_base = ord('A') - 1 # string이 나타낼 수 있는 아스키코드 최소값
    # count : 문자 개수 계산
    for item in array:
        letter = ord(item[col]) - min_base if col < len(item) else 0 # if. 현재 원소 길이 > 확인하고 싶은 문자열 인덱스 : 숫자 개수 count++, if. 현재 원소 길이 < 확인하고 싶은 문자열 인덱스 : 숫자 개수 0
        count[letter] += 1

    # count : 문자 개수 누적합 계산 -> output 배열에 sorting할 때, 해당 숫자가 어느 위치에 들어가야할지 파악 가능. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
    for i in range(len(count)-1):
        count[i + 1] += count[i]

    # B : sorting된 원소 담음. C가 B의 인덱스를 알려줌
    for item in reversed(array):
        letter = ord(item[col]) - min_base if col < len(item) else 0 # if. 현재 원소 길이 > 확인하고 싶은 문자열 인덱스 : 숫자 개수 count++, if. 현재 원소 길이 < 확인하고 싶은 문자열 인덱스 : 숫자 개수 0
        output[count[letter] - 1] = item # output 배열의 인덱스 0번부터 값을 넣기 위해. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
        count[letter] -= 1 # 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦

    return output

def radix_sort(array, max_count = None):
    # 길이가 가장 긴 문자열 반환
    if (len(array) != 0):
        if not max_count:
            max_count = len(max(array, key = len)) # max(array, key = len) : string의 관점에서 배열에서 최대값을 갖는 원소 추출

        # 각 원소의 마지막 문자 -> 각 원소의 처음 문자 순으로 비교 + 정렬
        for cnt in range(max_count-1, -1, -1): # max_len-1, max_len-2, ..., 0
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
    arr = radix_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")