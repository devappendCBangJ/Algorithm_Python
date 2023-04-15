import time

def quick_sort(arr):
    def sort(low, high):
        if(low < high): # low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
            # pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류. reculsive하게 반복(pivot 자체는 sorting에 참여 x)
            partition(low, high)

            # 배열 2등분 reculsive하게 반복
            sort(low, m1 - 1)
            sort(m1 + 1, m2 - 1)
            sort(m2 + 1, high)

    def partition(low, high):
        global m1
        global m2
        pivot1 = arr[low] # pivot 선택
        pivot2 = arr[(low+high)//2]
        m1 = low # S1, S2가 비워진 상태에서 시작
        m2 = (low+high)//2

        for k in range(low + 1, m2 + 1): # pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 순회 ♣
            if(arr[k] < pivot1): # case2(pivot보다 더 작은 원소인 경우) : swap o, case1(pivot보다 더 큰 원소인 경우) : swap x
                m1 += 1
                arr[k], arr[m1] = arr[m1], arr[k]
            else:
                pass
        for k in range(m2 + 1, high + 1): # pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 순회 ♣
            if(arr[k] < pivot2): # case2(pivot보다 더 작은 원소인 경우) : swap o, case1(pivot보다 더 큰 원소인 경우) : swap x
                m2 += 1
                arr[k], arr[m2] = arr[m2], arr[k]
            else:
                pass
        pivot1, arr[m1] = arr[m1], pivot1  # pivot1 위치로 swap o
        pivot2, arr[m2] = arr[m2], pivot2  # pivot2 위치로 swap o

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
    quick_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")