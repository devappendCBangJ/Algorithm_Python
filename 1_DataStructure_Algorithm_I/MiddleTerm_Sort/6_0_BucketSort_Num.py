import time

def bucket_sort(input_list):
    # bucket list의 size 범위 설정
    max_value = max(input_list)
    size = max_value / len(input_list)

    # input list와 크기가 같은 2차원 bucket list 생성(bucket의 크기를 input list의 크기와 같은 것을 사용하겠다!)
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([]) # [[], [], [], [], []]꼴 2차원 배열 생성
    # print(buckets_list) # 확인용 코드

    # 해당 bucket list에 input list의 원소 분류
    for i in range(len(input_list)):
        j = int(input_list[i] / size) # int(input_list[i] / size) : 원소값 / bucket 1개의 크기 = 담아야할 bucket의 index
        if j != len(input_list): # j가 max_value가 아닌 경우 : 담아야할 bucket의 index에 맞게 원소값 넣음
            buckets_list[j].append(input_list[i])
        else: # j가 max_value인 경우 : 원소값 / bucket 1개의 크기를 했을 때, 나머지가 없이 몫이 딱 나눠 떨어져버림. 그래서 몫이 딱 나눠 떨어져버려서 bucket의 개수를 벗어나는 index를 가지게 됨. bucket의 마지막 index에 원소값 넣음
            # print(j) # 확인용 코드
            buckets_list[len(input_list) - 1].append(input_list[i])
        # print(buckets_list) # 확인용 코드

    # bucket list별로 삽입 정렬
    for z in range(len(buckets_list)): # len(input_list) = len(buckets_list) : input list의 개수와 buckets list의 개수를 같게 생성했으므로 이렇게 써도 된다
        insertion_sort(buckets_list[z])

    # bucket list의 결과 합치기
    final_output = []
    for x in range(len(buckets_list)): # len(input_list) = len(buckets_list) : input list의 개수와 buckets list의 개수를 같게 생성했으므로 이렇게 써도 된다
        final_output = final_output + buckets_list[x]
    return final_output

def insertion_sort(bucket):
    for i in range (1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

input_list = [1.20, 0.22, 0.43, 0.36,0.39,0.27, 0.0]
print('ORIGINAL LIST:')
print(input_list)
sorted_list = bucket_sort(input_list)
print('SORTED LIST:')
print(sorted_list)

start = time.time_ns()
bucket_sort(input_list)
end = time.time_ns()