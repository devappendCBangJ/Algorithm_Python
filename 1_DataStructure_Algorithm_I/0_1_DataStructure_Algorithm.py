"""
○ 알고리즘
    ● Sorting
        0. Divide and Conquer Method
            1) divide step : 큰 문제를 작은 문제로 쪼개서 각각 해결(reculsive)
            2) conquer step : 작은 문제를 큰 문제로 합치면서 해결
            - 알고리즘 측면에서 자주 쓰이는 방법
        1. Sorting 종류
            1) Comparison Based Sort - Iterative Based Sort
                (1) Bubble Sort
                    1] 개념
                        앞뒤 원소 비교 + 스왑
                    2] 알고리즘
                        [1] 앞뒤 원소 비교
                        [2] 스왑
                            0(처음 인덱스) ~ N-1(마지막 인덱스까지의 원소들)
                            0(처음 인덱스) ~ N-2(정렬된 원소를 제외한 원소들)
                            0 ~ N-3 ...
                        [3] 반복
                        - 정렬 : 마지막 인덱스부터 정렬
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] stable : 동점자 처리 시 서로의 순서 유지
                (2) Insertion Sort
                    1] 개념
                        원소 선택 + 앞쪽 덩어리에서 순서에 맞게 배치
                    2] 알고리즘
                        [1] 1개 원소 선택
                        [2] 해당 원소 앞쪽 덩어리 원소들과 비교
                        [3] 밀어내기
                        [4] 반복
                        - 정렬 : 선택한 원소의 앞쪽 덩어리 내에서 정렬
                        - 밀어내기 : 앞쪽 덩어리의 마지막 원소부터 처음 원소 순으로 비교
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] stable : 동점자 처리 시 서로의 순서 유지
                (3) Selection Sort
                    1] 개념
                        최소값부터 정렬
                    2] 알고리즘
                        [1] 앞뒤 원소 비교 반복
                        [2] 최소값 찾기
                        [3] 다 돌면 스왑
                        [4] 반복
                        - 정렬 : 첫 인덱스부터 정렬
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] not stable : swap 사용 - 동점자 처리 시 순서 바꿀수 있으므로 not stable
            2) Comparison Based Sort - Recursive Based Sort
                (1) Merge Sort
                    1] 개념
                        배열 2등분 반복(1개로 쪼개질때까지 reculsive) + 2등분된 조각들 비교하여 sorting하면서 merge 반복
                    2] 알고리즘(devide and conquer)
                        [1] 배열 2등분 반복(1개로 쪼개질때까지 reculsive)
                        [2] 2등분된 배열 조각들끼리 원소들간 비교 + sorting + merge 반복
                        - 정렬 : 조각조각 정렬 + merge
                    3] 특징
                        [0] devide and conquer 방식
                        [1] 시간복잡도 : O(nlogn)
                            1]] merge 1회(1 depth)
                                - 총 원소 개수 n = high - low + 1
                                - 비교 <= n - 1 ♣ 왜 이건지는 모르겠다
                                - 기존배열에서 임시 배열로 이동 = n
                                - 임시배열에서 기존 배열로 이동 = n
                                >> 3n-1 = O(n)
                            2]] merge 횟수(전체 depth)... 시간복잡도가 이것에 의존적 ♣
                                >> O(logn)
                            3]] 총 시간 복잡도
                                >> O(nlogn) = O(n) x O(logn)
                        [2] not inplace : 추가 메모리 사용o
                        [3] stable : 동점자 처리 시 서로의 순서 유지

                        [1] 장점
                            1]] 동일한 속도 : original 배열의 순서에 관계없이 항상 동일한 속도
                            2]] 빠른 속도 : 매우 많은 원소에 유용
                        [2] 단점
                            1]] 구현 어려움
                            2]] not inplace : merge 과정에서 O(n) 수준 추가 메모리 사용
                    4] 구현 in C언어
                        // 전체 함수
                        void mergeSort(int a[], int low, int high){
                            if(low < high){ // low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
                                // 배열 2등분 reculsive하게 반복
                                int mid = (low+high)/2;
                                mergeSort(a, low, mid);
                                mergeSort(a, mid+1, high);

                                // 2등분된 배열 조각들끼리 원소들간 비교 + sorting + merge 반복
                                merge(a, low, mid, high);
                            }
                        }

                        // merge 함수
                        void merge(int a[], int low, int mid, int high){
                            int n = high - low + 1; // 배열 원소 개수
                            int* b = new int[n]; // 임시 배열
                            int left = low, right = mid + 1, bIdx = 0; // 초기값

                            while(left <= mid && right <= high){ // 배열 절반 쪼갬. 두 배열끼리 첫번째 인덱스부터 비교. 작은 것을 임시배열에 담음
                                if(a[left] <= a[right])
                                    b[bIdx++] = a[left++];
                                else
                                    b[bIdx++] = a[right++];
                            }
                            while(left <= mid) b[bIdx++] = a[left++]; // 두 배열 중 한 배열이 남으면 전부 순서대로 임시배열에 담음
                            while(right <= high) b[bIdx++] = a[right++];

                            for(int k = 0; k < n; k++) // 임시 배열 원소를 기존 배열로 붙여넣기
                                a[low+k] = b[k];
                            delete [] b; // 임시배열 삭제
                        }
                (2) Quick Sort
                    1] 개념
                        pivot 선택 + 구역에 맞게 분류 + 2등분 반복
                    2] 알고리즘
                        [1] pivot 선택
                        [2] 스왑을 통해 pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류(pivot 자체는 sorting에 참여 x)
                        [3] pivot도 본인 위치로 스왑
                        [4] pivot 기준 배열 2등분
                        [5] 위 과정 반복
                        [6] merge
                        - 정렬 : 조각조각 내면서 분류하여, 결국 정렬
                    3] 특징
                        [0] devide and conquer 형식
                        [1] 시간복잡도 : 최악 : O(n^2) / average : O(nlogn)
                            1]] partition 1회(1 depth)
                                - 총 원소 개수 n = high - low
                                >> O(n)
                            2]] partition 횟수(전체 depth)... 시간복잡도가 이것에 의존적 ♣
                                - 배열이 이미 오름차순 정렬 되어있음 + pivot으로 첫번째 원소를 사용
                                >> O(n)
                                - pivot으로 분류할때마다 pivot에 의해 두개의 구역이 정확히 반으로 갈라짐
                                >> O(logn)
                            3]] 총 시간 복잡도
                                - 배열이 이미 오름차순 정렬 되어있음 + pivot으로 첫번재 원소를 사용
                                >> O(n^2)
                                - pivot으로 분류할때마다 pivot에 의해 두개의 구역이 정확히 반으로 갈라짐
                                >> O(nlogn)
                        [2] inplace : 추가 메모리 사용x
                        [3] not stable : swap 사용 - 동점자 처리 시 순서 바꿀수 있으므로 not stable
                    4] 구현 in C언어
                        // 전체 함수
                        void quickSort(int a[], int low, int high){
                            if(low < high){ // low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
                                // pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류. reculsive하게 반복(pivot 자체는 sorting에 참여 x)
                                int pivotIdx = partition(a, low, high); // 아무거나 선택하면 된다

                                // 배열 2등분 reculsive하게 반복
                                quickSort(a, low, pivotIdx - 1);
                                quickSort(a, pivotIdx + 1, high);
                            }
                        }

                        // partition 함수
                        int partition(int a[], int i, int j){
                            int p = a[i]; // pivot 선택
                            int m = i; // S1, S2가 비워진 상태에서 시작

                            for(int k = i + 1; k <= j; k++){ // pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 반복 ♣
                                if(a[k] < p){ // case2(pivot보다 더 작은 원소인 경우) : swap o
                                    m++;
                                    swap(a[k], a[m]);
                                }
                                else{ // case1(pivot보다 더 큰 원소인 경우) : swap x
                                }
                            }
                            swap(a[i], a[m]); // pivot
                            return m;
                        }
            3) Not Comparison Based Sort
                (1) Bucket Sort
                    1] 개념
                        bucket으로 나누어 각각 정렬
                    2] 알고리즘
                        [1] bucket 기준 선택 + 배열 생성
                        [2] bucket에 원소 담기
                        [3] bucket 내에서 각각 정렬
                            - bucket 내에서 comparison 존재할 수 있다.
                        [4] merge
                    3] 특징
                        [1] 시간복잡도 : ???
                        [2] not inplace : 추가 메모리 사용o
                        [3] ???
                (2) Radix Sort
                    1] 개념
                        각 자리 숫자에 대한 grouping 반복
                    2] 알고리즘
                        [1] 최대 자릿수인 원소 찾기
                        [2] 최대 자릿수만큼 아래의 과정 반복
                        [3] 1의 자리수부터 최대 자리수까지 한 자리씩 원소 정렬 + 원소 합치기
                    3] 특징
                        [1] 시간복잡도 : O(dn)
                            - d가 작은 경우 : O(n) 수준
                            - 대부분 경우 : O(nlogn) 수준
                        [2] not inplace : 추가 메모리 사용o
                        [3] stable : 동점자 처리 시 서로의 순서 유지

                        [1] 몇째 자리부터 grouping 해야하는지는 상관x
                    4] 구현 in C언어
                        // v : 데이터 담긴 배열
                        // digit : 데이터 특정 자리수의 값
                        // digitQueue : 데이터 특정 자리수의 값을 인덱스로 하는 임시 배열
                        // power : 숫자의 자리수 지정
                        // d : 데이터의 최대 자리수

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
        2. Sorting 요약
            종류 : Worst Case / Best Case / Inplace / stable
            Bubble Sort : O(n^2) / O(n^2) / yes / yes ♣♣♣ 스왑 있는데 stable 맞나???
            Bubble Sort2 : O(n^2) / O(n) / yes / yes
            Insertion Sort : O(n^2) / O(n) / yes / yes ♣♣♣ temp에 insert할 원소 넣어두는데 inplace 맞나???
            Selection Sort : O(n^2) / O(n^2) / yes / no

            Merge Sort : O(nlogn) / O(nlogn) / no / yes
            Quick Sort : O(n^2) / O(nlogn) / yes / no

            Radix Sort : O(dn) / O(dn) / no / yes

    ● Recursion
        1) 개념 : method가 자기 자신을 call
        2) case
            (1) base case : 재귀 호출 없이 답 추출 가능한 경우
                - base case에 대한 정의가 중요하다
                - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
            (2) recursive case : 재귀 호출을 써야 답 추출 가능한 경우
        3) 예시 알고리즘
            (1) factorial
                1] 개념
                    n! = 1 * 2 * 3 *... * (n-1) * n
                2] 함수 정의
                    f(n) = 1            if n=0
                    f(n) = n * f(n-1)   else
                3] 코드 구현
                    def factorial(n):
                        if n == 0:
                            return 1
                        else:
                            return n * factorial(n-1)
            (2) english ruler ♣♣
                1] 개념 : 눈금자 그리기
                2] 일부 구현
                    drawTicks(length)
                        if(length > 0) then
                            drawTicks(length - 1)
                            주어진 length의 tick을 draw
                            drawTicks(length - 1)
                3] 전체 구현
                    # 선 그리기
                    def draw_line(tic_length, tick_label = ''):
                        line = '-' * tick_length
                        if tick_label:
                            line += ' ' + tick_label
                        print(line)

                    # recursive
                    def draw_interval(center_length):
                        if center_length > 0:
                            draw_interval(center_length - 1)
                            draw_line(center_length)
                            draw_interval(center_length - 1)

                    # 전체 함수 ♣♣
                    def draw_ruler(num_inches, major_length):
                        draw_line(major_length, '0') # 0 표시
                        for j in range(1, 1 + num_inches):
                            draw_interval(major_length - 1)
                            draw_line(major_length, str(j)) # 1, 2, 3,... 표시
            (3) binary search ♣♣
                1] 개념 : 정렬되어있는 list에서 원소 탐색
                2] 알고리즘
                    target == data[mid] : target 찾기 완료
                    target < data[mid] : mid 앞 덩어리 recur
                    target > data[mid] : mid 뒷 덩어리 recur
                3] 전체 구현
                    def binary_search(data, target, low, high):
                        if low > high: ♣♣
                            return False
                        else:
                            mid = (low + high) // 2
                            if target == data[mid]:
                                return True
                            elif target < data[mid]:
                                return binary_search(data, target, low, mid-1)
                            else:
                                return binary_search(data, target, mid+1, high)
                4] 특징
                    [1] 시간복잡도 : O(logn)
                        1회 비교 시 수행시간 ♣♣♣ 뭔소리???
                        (mid-1)-low+1 = (low+high)/2-low <= (high-low+1)/2
                        high-(mid+1)+1 = high-(low+high)/2 <= (high-low+1)/2
        4) 종류
            (1) linear recursion
                1] case
                    [1] base case : 재귀 호출 없이 답 추출 가능한 경우
                        - base case에 대한 정의가 중요하다
                        - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
                    [2] recursive case : 재귀 호출을 써야 답 추출 가능한 경우
                        - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
                        - 재귀적 호출 중 어떤 호출이 필요한지 판단과정이 있을 수 있지만, 궁극적으로 하나의 재귀 호출만 수행해야함
                2] 예시 알고리즘
                    [1] linear sum
                        1]] 알고리즘
                            Algorithm LinearSum(A, n):
                                # A : 배열
                                # n : 원소 개수
                                # output : 배열에서 n번째 원소까지의 합
                                if n = 1 then ♣
                                    return A[0]
                                else ♣♣ else니까 n이 1일 때는 여기로 들어오지 않는다. n이 2 이상일때만 여기로 들어온다
                                    return LinearSum(A, n-1) + A[n-1]

                            -> for문으로 짜도 된다
                    [2] reverse array
                        1]] 알고리즘
                            Algorithm ReverseArray(A, i, j):
                                # A : 배열
                                # i : 앞쪽에서 오는 원소 인덱스
                                # j : 뒤쪽에서 오는 원소 인덱스
                                # output : 배열 앞 뒤 원소 reverse
                                if i < j then
                                    swap A[i] and A[j]
                                    ReverseArray(A, i+1, j-1)
                                return

                            -> for문으로 짜도 된다
                        2]] 코드 구현
                            def reverse(S, start, stop):
                                if start < stop-1: # 배열 인덱스가 0부터 시작하기 때문에 stop-1이 마지막 원소 인덱스 ♣♣♣
                                    S[start], S[stop-1] = S[stop-1], S[start]
                                    reverse(S, start+1, stop-1)

                            -> for문으로 짜도 된다
                    [3] power
                        1]] 알고리즘1
                            P(x, n) = x^n

                            P(x, n) = 1                 (if n = 0)
                            P(x, n) = x * p(x, n-1)     (else)

                            -> 시간 복잡도 : O(n) ♣♣♣
                            -> for문으로 짜도 된다
                        2]] 알고리즘2
                            P(x, n) = 1                     (if n = 0)
                            P(x, n) = x * (P(x, (n-1)/2)^2)   (if n > 0 is odd)
                            P(x, n) = p(x, n/2)^2           (if n > 0 is even)

                            Algorithm Power(x, n):
                                # x : 밑
                                # n : 지수
                                # output : x^n
                                if n = 0 then
                                    return 1
                                if n is odd then
                                    y = power(x, (n-1)/2)   # O(logn)
                                    return x * y * y
                                else
                                    y = power(x, n/2)       # O(logn)
                                    return y * y

                            -> 시간 복잡도 : O(logn)
                            -> for문으로 짜도 된다
            (2) tail recursion
                1] 개념 : last step에서 recursive call 발생
                2] 예시 알고리즘
                    Algorithm IterativeReverseArray(A, i, j):
                        # A : 배열
                        # i : 앞쪽에서 오는 원소 인덱스
                        # j : 뒤쪽에서 오는 원소 인덱스
                        # output : 배열 앞뒤 원소 reverse
                        while i < j do
                            Swap A[i] and A[j]
                            i = i + 1
                            j = j - 1
                        return IterativeReverseArray(A, i, j) # 바로 점프해서 속도 빠를 수 있다.
            (3) binary recursion
                1] 개념 : 각각의 non base case에서 2개 recursive call 발생
                2] 예시 알고리즘
                    [1] english ruler
                        drawTicks(length)
                            if(length > 0) then
                                drawTicks(length - 1)
                                주어진 length의 tick을 draw
                                drawTicks(length - 1)
                    [2] binary sum
                        Algorithm BinarySum(A, i, n):
                            # A : 배열
                            # i : 배열에서 원소 인덱스
                            # n : 분할되고 남은 원소 개수
                            # output : 배열에서 n번째 원소까지의 합
                            if n = 1 then
                                return A[i]
                            return BinarySum(A, i, n/2) + BinarySum(A, i + n/2, n/2) ♣♣♣ 강의자료 그림 확인
                    [3] fibonacci numbers 비효율적 방법 ♣♣♣
                        F_0 = 0
                        F_1 = 1
                        F_i = F_(i-1) + F_(i-2)         (if i > 1)

                        Algorithm BinaryFib(k):
                            # k : 피보나치 계산 횟수
                            # output : 피보나치 수 = F_k
                            if k = 1 then
                                return k
                            else
                                return BinaryFib(k-1) + BinaryFib(k-2) ♣♣♣

                        -> recursion 횟수 : n_k > 2^(k/2) ♣♣♣
                    [4] fibonacci numbers 효율적 방법 ♣♣♣
                        Algorithm LinearFib(k):
                            # k : 피보나치 계산 횟수
                            # output : 피보나치 수 쌍 = F_k, F_(k-1)
                            if k = 1 then
                                return (k, 0)
                            else
                                (i, j) = LinearFib(k-1) ♣♣♣
                                return (i+j, i)

                        -> recursion 횟수 : n_k = k-1 ♣♣♣
            (4) multiple recursion 
                1] 개념 : 많은 recursive call 발생(1 or 2번이 아님)
                2] 예시
                    [1] summation puzzles ♣♣♣ 뭔소리??? 강의자료 확인
                        pot + pan = bib     // 421 + 437 = 858 (p=4, o=2, t=1, a=3, n=7, b=8, i=5)
                        dog + cat = pig
                        boy + girl = baby

    ● Hash Tables
        1. Map
            1) 특징 ♣♣♣
                (1) 검색가능한 key-value pairs items의 집단
                (2) 활용 : searching, inserting, deleting 등
                (3) 같은 key의 여러 item 허용x
            2) 예시
                ex1. address book
                ex2. student-record database
                ex3. python의 dict class
                ex4. 비트 코인
                ex5. 전자 증명서(공인 인증 등...)
            3) ADT
                M[k] : map M에서 key k와 관련된 value v return
                M[k] = v : map M에서 key k와 관련된 value v를 replacing
                del M[k] : map M에서 key k와 관련된 item remove
                len(M) : map M에서 item의 개수
                iter(M) : map M에서 key 순서대로 순회
                k in M : map M에 key k 존재 시, true return ♣♣
                M.get(k, d=None) : map M에 key k 존재 시, value v return / 그렇지 않은 경우, value d return ♣♣
                M.setdefault(k, d) : map M에 key k 존재 시, value v return / 그렇지 않은 경우, M[k] = d 대입 + value d return ♣♣
                M.pop(k, d=None) : map M에서 key k와 관련된 item remove + value v return / 그렇지 않은 경우, value d return ♣♣
            4) ADT 예시
                - 강의자료 참조
            5) 구현
                (1) Simple List-Based Map ♣♣
                    1] 특징
                        [1] 구현 : unsorted list로 구현 ♣♣♣
                        [2] 유용한 경우 ♣♣♣
                            - 작은 size의 map
                            - insertion 자주 발생하는 map
                            - searching, removing 거의 발생하지 않는 map
                    2] 시간복잡도
                        [1] inserting : O(1)
                            - insertion 시 중복 key값 체크하지 않는 경우만 O(1)
                            - insertion 시 중복 key값 체크 시 시간복잡도 증가
                        [2] searching : O(n)
                        [3] removing : O(n)
                (2) Hash Tables
                    1] hash function(h)
                        [1] 목적 : key를 넓게 분포시켜서 중복 방지(index 관리)
                        [2] 구조
                            h(x) = h2(h1(x))
                            1]] hash code
                                [[1]] 개념 ♣♣♣
                                    h1 : keys -> integers
                                [[2]] 활용 예시
                                    - Memory Address : 메모리 주소 활용
                                    - Integer Cast : key의 bit 활용
                                    - Component Sum : key의 bit 조각을 더함       (overflow 무시)
                                    - Polynomial accumulation : p(z) = a0 + a_1 * z_1 + a_2 * z_2 + ... + a_(n-1) * z_(n-1)     (overflow 무시)
                                        z : fixed value
                            2]] compression func
                                [[1]] 개념 ♣♣♣
                                    h2 : integers -> [0, N-1]
                                [[2]] 활용 예시
                                    - Division : h2(y) = y mod N
                                        N : 충돌 가능성 낮추기 위해 '소수' 사용 ♣♣♣
                                    - Multiply & Add & Divide(MAD) : h2(y) = (ay + b) mod N
                                        a, b : 음이 아닌 정수 ♣♣♣
                        [3] 예시
                            1]] SSN(Social Security Number)
                                배열 크기 N = 10,000
                                h(x) = x의 마지막 4자리 수
                        [4] 성능
                            1]] collision의 개수와 높은 연관성
                            2]] 적절한 수치 선택 by 목적
                                [[1]] collision감소, address space증가
                                    ex. data개수 << N개수
                                [[2]] collision증가, address space감소
                                    ex. data개수 = N개수
                        [5] 코드 구현
                            강의자료 참조
                    2] Collision Handling
                        [1] 개념 : 서로 다른 원소가 같은 cell에 map되었을 때 대처
                        [2] 종류
                            1]] Separate Chaining
                                [[1]] 개념 : 충돌 item을 linked list로 연결 ♣♣♣
                                [[2]] 특징
                                    - 간단한 구현
                                    - 추가 메모리 필요
                                [[3]] 알고리즘 ♣♣♣
                                    Algorithm get(k)
                                        return A[h(k)].get(k)
                                    Algorithm put(k, v)
                                        t = A[h(k)].put(k, v)
                                        if t = null then        (k is a new key) ♣♣♣
                                            n = n + 1
                                        return t
                                    Algorithm remove(k)
                                        t = A[h(k)].remove(k)
                                        if t != null then       (k was found) ♣♣♣
                                            n = n - 1
                                        return t
                                [[4]] 코드 구현
                                    강의자료 참조
                            2]] Open Addressing - Linear Probing
                                [[1]] 개념 : 충돌 item을 다음 남은 table cell에 넣음 ♣♣♣
                                [[2]] 예시
                                    h(x) = x mod 13
                                    insert key : 18, 41, 22, 44, 59, 32, 31, 73

                                    18 -> 5
                                    41 -> 2
                                    22 -> 9
                                    44 -> 5 -> 6
                                    59 -> 7
                                    32 -> 6 -> 7 -> 8
                                    31 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
                                    73 -> 8 -> 9 -> 10 -> 11
                                [[3]] 알고리즘 ♣♣♣
                                    1]]] Searching ♣♣♣
                                        Algorithm get(k)
                                            i <- h(k)
                                            p <- 0
                                            repeat
                                                c <- A[i]
                                                if c = null                 // 해당 item 존재x 시, null 반환
                                                    return null
                                                else if c.getKey() = k      // 해당 item 존재o + key 일치o 시, value 반환
                                                    return c.getValue()
                                                else                        // 해당 item 존재o + key 일치x 시, i와 p 증가시키면서 반복
                                                    i <- (i + 1) mod N
                                                    p <- p + 1
                                            until p = N                     // p 개수가 배열 개수와 같아질때까지 반복
                                            return null
                                    2]]] updating ♣♣♣
                                        key k 탐색
                                            (k, o) 발견 시, 삭제하지 않음. special item인 available로 바꿈
                                                이렇게 해서 나중에 Searching 할 때, An empty cell is found가 되지 않도록 함
                                                + 나중에 Inserting 할 때, available에도 data 넣을 수 있도록 함
                                    3]]] put(k, o)
                                        Algorithm put(k, o)
                                [[4]] 코드 구현
                                    강의자료 참조
                            3]] Open Addressing - Double Hashing(Double Probing) ♣♣♣
                                [[1]] 개념 : 2개 hash func 사용 + 충돌 item을 다음 남은 table cell에 넣음
                                    1]]] 기준1(충돌 없을 시 사용) : h(k) = k mod N
                                    2]]] 기준2(충돌 시 사용) : (i + jd(k)) mod N     // d(k) >= 0
                                        - d(k) = (q - k) mod q

                                     k : key
                                     N : 배열 개수
                                     q : 사용자 임의 지정
                                     i : key
                                     j : 사용자 임의 지정
                                [[2]] 특징
                                    - 시간 복잡도 ♣♣♣
                                        Searching, Inserting, Removing on Hash table
                                        최악 : O(n) # 거의 이런 경우 없다
                                        대부분 : O(1) # 거의 이와 가깝다
                                        
                                        - 실제 경우에서 매우 빠르다
                                [[3]] 비교 ♣♣♣
                                    - linear probing : 한 뭉탱이로 data 몰려있으면 probing 연산 증가
                                    - double probing : 한 뭉탱이로 data 몰려있어도 점프해서 data 넣기 때문에 probing 연산 감소
                                [[4]] 예시 ♣♣♣
                                    ex1. Small Database
                                    ex2. Compilers
                                    ex3. Browser Caches
                                [[4]] 예시 ♣♣♣
                                    강의자료 참조

    ● Skip List
        1) 특징 ♣♣
            (1) special key 포함 : -∞ ~ +∞ 포함
            (2) key 정렬 : 오름차순
            (3) list별 포함 관계 : S_h ⊂ ... S_1 ⊂ S_0
            (4) 구현 : quad node 활용
            (5) 시간복잡도 : O(nlogn) ♣♣♣
        2) 알고리즘 ♣♣♣
            (1) Searching
                - x의 위치를 찾고자함
                1] top list의 첫번째 위치 p부터 탐색
                2] 현재 위치 p에서 x <-> y = key(next(p)) 비교
                    [1] x = y : return element(next(p))
                    [2] x > y : scan forward
                    [3] x < y : drop down
            (2) Insertion
                강의자료 참조
            (3) Deletion
                강의자료 참조

    ● Search Trees ♣♣♣
        1. Binary search trees
            1) 개요
                (1) Ordered Maps ♣♣♣
                    1] 개념 : key 기준으로 sorting된 map
                    2] 특징
                        [1] 원하는 key인 k에 가장 가까운 기존 item 내의 key 추출 가능
                            - k보다 작거나 같은 가장 큰 key인 item
                            - k보다 크거나 같은 가장 작은 key인 item
                (2) Binary Search
                    1] 개념 : 배열로 구현된 ordered maps(key 기준 sorting된 map)에서 search
                    2] 특징
                        [1] 시간복잡도 : O(logn)
                (3) Search Tables ♣♣♣
                    1] 개념 : 배열로 구현된 ordered maps(key 기준 sorting된 map)에서 search
                    2] 특징
                        [1] 시간복잡도
                            - searching : O(logn) ♣♣♣
                            - inserting : n/2 -> O(n)
                            - removing : n/2 -> O(n)
                        [2] 성능
                            - 작은 크기 ordered maps : 높은 성능
                            - 큰 크기 ordered maps : 낮은 성능

                            - search 빈도 높음 + insertion, remove 빈도 낮음 : 높은 성능
                                ex. 사전, 피보나치 수열의 값 저장 등
                            - search 빈도 낮음 + insertion, remove 빈도 높음 : 낮은 성능
                (4) Binary Search Tree ♣♣♣
                    1] 개념 : node에 key or [key-value items]를 binary tree에 저장한 tree
                    2] 특징 ♣♣♣
                        [1] key(u) <= key(v) <= key(w)
                            - u : v의 왼쪽 subtree
                            - w : v의 오른쪽 subtree
                            - 왼쪽 node, 오른쪽 node에서 비교할 수 있는 관계 성립 ♣
                        [2] external node : item 저장x ♣
                        [3] inorder traversal : key 오름차순 방문
            2) 알고리즘
                (1) Search
                    Algorithm TreeSearch(T, p, k)
                        if (k == p.key()) then                                  // k가 p.key와 같으면 성공
                            return p
                        else if k < p.key() and T.left(p) is not None then      // k가 p.key보다 작은 경우 recursive 반복
                            return TreeSearch(T, T.left(p), k)
                        else if k > p.key() and T.right(p) is not None then     // k가 p.key보다 큰 경우 recursive 반복
                            return TreeSearch(T, T.right(p), k)
                        return p                                                // k와 정확히 같은값 찾기 실패
                (2) Insertion ♣♣♣
                    - put(k, o)
                    - k를 node w에 insert + w를 internal node로 확장(w의 leaf가 없으면 추가)

                    Algorithm TreeInsert(T, k, v)
                        p = TreeSearch(T, T.root(), k)
                        if k == p.key() then
                            p의 값을 v로 설정
                        else if k < p.key()
                            item (k, v)인 node를 p의 왼쪽 자식에 추가
                        else if k > p.key()
                            item (k, v)인 node를 p의 오른쪽 자식에 추가
                (3) Deletion ♣♣♣
                    - key k가 v node에 저장되어있다고 생각하고, k 지우는 경우 생각
                    - v node가 leaf child인 w를 가지고 있다면, v와 w 제거
                    - removeExternal(w)

                    - inorder traversal을 통해 v의 뒷순서인 internal node w를 inorder traversal로 찾기 ♣♣♣
                    -> key(w)를 node v에 복사
                    -> node w, node w의 leaf child z 제거 = removeExternal(z)
                (4) 성능
                    1] 시간복잡도
                        - space : O(n)
                        - search : O(h) ♣♣♣
                        - update : O(h) ♣♣♣
                        - height : 최악 O(n) / 최선 O(logn) ♣

                        n : ordered map item 개수
                        h : binary search tree height

        2. Balanced search trees
            1) 개념 ♣♣
                - Standard Binary Search Tree 시간복잡도 : 최악 O(n) / 최선 O(logn)
                - Balanced Search Tree : Restructuring -> 항상 O(logn)
            2) 종류
                (1) AVL Trees
                (2) Splay Trees
                (3) (2, 4) Trees
                (4) Red-Black Trees

                (1) AVL Trees ♣♣♣
                    1] 특징
                        [1] Binary Search Tree
                        [2] 형제 위치에 있는 internal node간 자식 높이차 : 1이 최대
                        [3] leaf : placeholder 역할o. item 저장x
                    2] 동작
                        [1] Insertion
                            - External node의 확장 발생
                                -> imbalance 발생
                                -> restructuring 필요
                        [2] Deletion
                            - External node의 제거 발생
                                -> imbalance 발생
                                -> rebalancing 필요
                            - Rebalancing
                                제거된 node의 부모 node부터 traveling up해서 첫번째 unbalanced node 찾기 ♣♣♣
                                -> 해당 unbalanced node 기준으로 더 큰 높이를 가진 자식 node가 올라가도록 Rotation ♣♣♣
                        [3] Restructuring
                            - 형제 위치에 있는 internal node간 자식 높이차가 2 이상일 때, 자식의 높이가 더 큰쪽을 위로 올림.
                                만약, [왼쪽에 있는 자식]을 [부모]로 올리려면, [왼쪽에 있는 자식]의 [오른쪽에 자식]이 있으면 안된다.
                                이런 경우에는 [왼쪽에 있는 자식의 오른쪽에 해당하는 자식]을 2번 rotation해서 [부모] 위치까지 올린다.
                            - 반대의 경우도 좌우를 바꿔서 생각하면 된다 ♣♣♣ 바닥에서부터 규칙이 깨진 지점을 찾아 올라갈때, 가장 먼저 나온 깨진 지점만 보면 된다

                            1]] Single rotation
                            2]] Double rotation
                    3] 예시
                        강의자료 참조
                (2) Splay Trees ♣♣♣
                    1] 개념 of Splaying
                        - 새로운 node 들어오면, root node로 올림
                    2] 특징
                        [1] Binary Search Tree
                            - 자료 저장 : internal node에 저장
                            - 왼쪽 하위 트리 key <= v의 key <= 오른쪽 하위 트리 key
                        [2] 모든 Operation 이후, Rotation 수행
                        [3] 시간복잡도 : O(h) ♣♣♣
                            - 최악 시간복잡도 : O(n)
                            - 최선 시간복잡도 : O(1)
                            - 많은 경우 O(1) but 최악 O(n)이므로 속도 일정x. real-time system에서 사용하기 어려울 수 있음 ♣♣♣
                    3] 동작
                        [1] Zig = Right Rotation
                        [2] Zag = Left Rotation
                        [3] Zig + Zig
                        [4] Zag + Zag
                        [5] Zig + Zag
                    4] 예시
                        강의자료 참조
                (3) (2, 4) Trees ♣♣♣
                    1] 개념
                        - 2 ~ 4개 child 갖는 tree
                    2] 특징
                        [1] Binary Search Tree
                        [2] 2 ~ 4개 child 갖는 tree
                        [3] key 순서
                            k = k_i (i = 1, 2, ..., d-1)
                            k < k_i
                            k_(i-1) < k < k_i
                            k_(d-1) < k
                        [4] leaf : placeholder 역할o. item 저장x
                    3] 동작
                        [1] Inorder Traversal
                            - 오름차순 순차적 방문
                        [2] Searching
                            1]] k = k_i (i = 1, 2, ..., d-1) : 탐색 완료
                            2]] k < k_1 : 자식 node v_1에서 탐색 이어감
                            3]] k_(i-1) < k < k_i : 자식 node v_i에서 탐색 이어감
                            4]] k_(d-1) < k : 자식 node v_d에서 탐색 이어감
                        [3] Insertion
                            if. 5 node : overflow + split
                        [4] Deletion
                            if. empty node : underflow + fusion
                    4] 예시
                        강의자료 참조
                (4) Red-Black Trees ♣♣♣
                    1] 개념
                        - (2, 4) tree를 balanced binary tree로 나타내기 위해 red, black node 개념 추가
                            red node : 동일 계층
                            black node : 상하 계층
                    2] 특징
                        [1] 구조 : Binary Tree
                        [2] Color 특징
                            1]] Root : 항상 black
                            2]] Leaf : 항상 black
                            3]] red node의 자식 : 항상 black (no double red)
                            4]] depth : 모든 leaf에서 항상 같은 black depth ♣♣♣
                        [3] 시간복잡도 : O(logn) 일정 ♣♣♣
                    3] 동작
                        [1] Insertion
                            if. Child-Parent사이 Double Red 발생
                                1]] Restructuring
                                    - 형제 위치는 검정인 경우
                                    - (2, 4) tree Restructuring과 동일
                                    - (2, 4) tree 관점에서 형태 유지
                                2]] Recoloring
                                    - 형제 위치도 빨강인 경우
                                    - 부모 node가 root가 아니면 red로 변경 + 형제 node 둘다 black으로 변경
                                    - (2, 4) tree 관점에서 split 발생
                        [2] Deletion
                            1]] Deletion 노드(부모 node) or 자식 node 빨강인 경우
                                - 자식 1개를 black으로 변환하여 남김
                            2]] Deletion 노드(부모 node) and 자식 node 검정인 경우
                                - 자식 1개를 double black으로 변환하여 남김
                                - double black : 모든 leaves가 같은 black depth를 가지지 않기 때문에, 규칙 위반
                                    -> Restructuring 실시 ♣♣♣


"""