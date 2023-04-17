import time

ord_base = 65 # A의 아스키코드(영어 문자 중에서 가장 작은 아스키코드)
ord_len = 58 # A~z 아스키코드 개수
def radix_sort(arr):
    # 길이가 가장 긴 문자열 반환
    max_len = len(max(arr, key = len)) # max(array, key = len) : string의 관점에서 배열에서 최대값을 갖는 원소 추출
    power = 0 # 가장 앞 문자부터 분류 시작
    temp = []
    for x in range(ord_len): # 임시 배열
        temp.append([]) # [[], [], [], [], []]꼴 2차원 배열 생성
    # print(temp) # 확인용 코드

    for i in range(max_len):
        distribute(arr, temp, power) # 데이터 그룹화 by power
        collect(temp, arr) # 데이터 재결합
        power += 1 # power 증가

def distribute(arr, temp, power): # 데이터의 특정 자리값 추출 + 그에 맞는 임시배열 index에 데이터 넣음
    for i in range(len(arr)):
        if(len(arr[i]) - 1 >= power): # 해당 데이터가 power보다 자리수가 같거나 많은 경우
            digit = (ord(arr[i][power]) - ord_base) % ord_len # 1의 자리부터 시작
            temp[digit].append(arr[i])
        else:
            digit = 0  # 1의 자리부터 시작
            temp[digit].append(arr[i])
    # print(temp) # 확인용 코드

def collect(temp, arr): # 임시배열의 데이터를 특정 자리값이 작은 순서부터 기존 배열에 넣음
    i = 0
    for digit in range(ord_len):
        while(len(temp[digit])>0):
            arr[i] = temp[digit].pop(0)
            i = i + 1
            # print(digit) # 확인용 코드
        # print(arr[digit]) # 확인용 코드

"""
// 전체 함수
void radixSort(vector<int> &v, int d){
    int power = 1; // 1의 자리부터 분류 시작
    queue<int> digitQueue(10); // 10자리 임시배열

    for(int i = 0; i < d; i++){
        distribute(v, digitQueue, power); // 데이터 그룹화 by power
        collect(digitQueue, v); // 데이터 재결합
        power *= 10; // power 증가
    }
}

// distribute 함수
void distribute(vector<int> &v, queue<int> digitQ(), int power){ // 데이터의 특정 자리값 판별 후 임시배열의 그에 맞는 index에 데이터 넣음
    int digit;
    for(int i = 0; i < v.size(); i++){
        digit = (v[i]/power) % 10; // 1의 자리부터 시작
        digitQ[digit].push(v[i]);
    }
}

// collect 함수
void collect(queue<int> digitQ[], vector<int> &v){ // 임시벡터의 데이터를 digit이 작은 순서부터 v배열에 다시 넣음
    int i = 0;
    int digit;

    for(digit = 0; digit < 10; digit++){
        while(!digitQ[digit].empty()){
            v[i] = digitQ[digit].front();
            digitQ[digit].pop();
            i++;
        }
    }
}
"""

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
    radix_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat  # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")