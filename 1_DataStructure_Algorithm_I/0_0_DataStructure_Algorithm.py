"""
● 데이터 구조 vs 알고리즘
    1. 데이터 구조
        1) 기본 자료 구조(Primitive Data Structure)
            (1)
                1] int
                2] char
                3] float
                4] double
        2) 추가 자료 구조(Non-Primitive Structure)
            (1) 선형(Linear)
                1] Array
                2] Stacks
                3] Queues
                4] (Linked)List
            (2) 비선형(Non-Linear)
                1] Tree
                2] Graphs
    2. 알고리즘
        1) 개념 : 특정 결과를 위한 규칙, 절차 수립
            - 입력 -> 알고리즘 -> 출력
        2) 특징
            (1) 명백한 모든 단계
            (2) 잘 정의된 데이터
            (3) 명확히 정의되어 이해하기 쉬움
        3) 알고리즘 분석(Algorithm Analysis)
            (1) 시간복잡도(Running Time)
                1] Seven Functions
                    [1] 1 : constant
                    [2] logn : logarithmic ♣
                    [3] n : linear
                    [4] nlogn : N-Log-N
                    [5] n^2 : quadratic ♣
                    [6] n^3 : cubic ♣
                    [7] 2^n : exponential ♣
                2] 시간복잡도(Counting Primitive Operations)
                    [1] Big-Oh Notation(최악 시간 복잡도)
                        - f(n) <= cg(n) for n >= n_0 ♣♣
                        - 큰 차수만 추출
                    [2] Big-Theta(평균 시간 복잡도) ♣
                        - c' g(n) <= f(n) <= c'' g(n) for n >= n_0 ♣♣
                    [3] Big-Omega(최선 시간 복잡도) ♣
                        - f(n) >= cg(n) for n >= n_0 ♣♣
            (2) 의사코드(Pseudocode)
                1] 고급 레벨 설명
                2] 소프트웨어, 하드웨어에 의존하지 않은 평가 ♣
    3. 객체지향 프로그래밍(Object Oriented Programming)
        1) 객체(Object)
            (1) 생성 : Class의 instance
            (2) 구성 : property & method
        2) 객체지향 원리(Object-Oriented Design Principles)
            (1) 특징
                1] 모듈화(Modularity)
                2] 추상화(Abstraction)
                3] 캡슐화(Encapsulation) : 은닉 가능
            (2) 과정
                1] Class 정의 : property & method 정의
                2] 생성자(Constructors) : instance 생성
                    - __init__ method로 불러옴
                3] 함수 오버로딩(Operator Overloading) : operation에 다양한 기능 부여
                4] 반복자(Iterators) : operation 반복
                    - __next__ : 다음 원소 return
                    - StopIteration : 다음 원소 없을 때, StopIteration

                    - __len__ : 원소 개수 return
                    - __getitem__ : 원소 index return ♣
                5] 상속(Inheritance)
                    [1] BaseClass : 부모 Class
                    [2] SubClass = ChildClass : 자식 Class가 부모 Class 상속

● 자료구조
    1. 튜토리얼
        1) 순환 알고리즘(Recursion Method)
            (1) 개념 : call 반복 >> return 반복
                def factorial(n): ♣
                    if n == 0:
                        return 1
                    else:
                        return n * factorial(n-1)
            (2) 예시
                1] 이진 탐색(Binary Search)
                    [1] 조건 : 정렬된 데이터
                    [2] 개념 : 절반씩 잘라서 탐색
                    [3] 특징
                        - Big-Oh : O(logn) ♣

    2. 메모리 관리(Memory manangement)
        1) Computer Architecture(x86)
            (1) 구조 ♣♣
                1] 부품
                    [1] Ports, CD-ROM, Floppy Drive
                    [2] RAM : 주소 저장. 휘발성o ♣
                    [3] ROM : 휘발성x
                    [4] register
                    [5] CPU

                    - 속도 좋은 것 : HDD < RAM < register
                    - 용량 : register < RAM < HDD
                2] 로더 ♣♣
                    1] 부트 로더(Boot Loader)
                    2] 프로그램 로더(Program Loader)
                        ex. excel
                    3] 클래스 로더(Class Loader)
                        ex. java의 class
                3] CPU ♣♣
                    CPU <-> RAM

                    - fetch & execute cycle
                    - 현재 프로그램 위치에 대한 indexing
                        1] page faults : page가 현재 RAM에 없는 경우
                            -> Virtual memory 사용 : idealized abstraction of the storage resources
                                Virtual memory <-> Physical memory

    3. List : Array-Based Sequences
        1) 저장 구조
            (1) sequence type : a set of memory locations
                [1] list
                [2] tuple
                [3] str

            (2) 종류
                1] array list
                    [1] 특징
                        - 쉬운 사용
                        - 확장 시 주의(메모리 관리 중요)
                    [2] 예시
                        1]] char arrays
                            [[1]] elements : store primitive elements
                            [[2]] reference : store references to objects
                        2]] intger arrays
                            [[1]] elements
                            [[2]] reference : 형식으로 저장하는 것보다 주소형태로 저장하는 것이 유리
                2] linked list
                    [1] 특징
                        - 유연한 확장
                    
        2) 활용
            (1) insertion
                - 해당 인덱스부터 한칸씩 뒤로 밀음 + 해당 원소 삽입
                - 시간복잡도 : O(n)
                    평균 : O(n/2)
            (2) remove
                - 해당 원소 제거 + 해당 인덱스 뒤부터 한칸씩 앞으로 당김
                - 시간복잡도 : O(n)
                    평균 : O(n/2)
            (3) 배열 확장 ♣♣
                1] Incremental strategy : size + constant c
                    - n + c + 2c + ... + kc = n + ck(k+1)/2
                    - T(n) = O(n + k^2)
                2] Doubling strategy : size x2
                    - T(n) = O(n)
            (4) 다차원 list

        3) list operations

    4. Stack
        0) ADT(Abstract Data Types) ♣♣
            (1) 정의 : 데이터 구조의 추상화
            (2) 특징
                - 저장된 데이터 명시
                - 데이터의 Operations 명시
                - Operations와 관련된 Error conditions 명시
        1) The Stack ADT
            (1) 특징
                - LIFO
                - 임시 객체 저장 ♣
            (2) Stack ADT
                1] Main Stack Operations
                    S.push(object)
                    S.pop()
                2] Auxiliary Stack Operations
                    S.top() = S.peek() ♣
                    len(S)
                    is_empty(S)
                    is_full(S)
        2) Stack Operations
            - Stack 설계에 따라 변화
            (1) Array-Based Stack ♣♣
                1] 특징 ♣♣
                    - 스택 저장 : array
                    - 자료저장 순서 : 왼쪽 -> 오른쪽
                    - 자료추출 순서 : 오른쪽 -> 왼쪽
                    - 변수 : top element의 index 추적
                    - 배열 확장
                        불가능 way : 기존 배열 + 새로운 배열 덧붙이기
                        가능 way : 더 큰 새로운 배열에 복사
                2] 시간 복잡도
                    - 최악 : O(n)
                    - pop : O(1)
                    - push : O(1)
                    [1] 단점 : 확장이 필요한 경우 block 단위 copy operation 필요
                        - 해킹에 활용 가능 ♣
                    [2] 장점 : 빠른 operation
        3) Application of Stacks
            (1) Applications Ex
                1] Direct applications
                    ex1. Page-visited history
                    ex2. undo sequence in text editor
                    ex3. chain of method calls in supports recursion ♣
                2] Indirect applications ♣♣
                    ex4. Auxiliary data structure for algorithms
                    ex5. Component of other data structures
            (2) Algorithm Ex ♣♣♣ 강의자료
                ex1. Parentheses Matching
                    - stack pair
                    push : < [ { (
                    pop : > ] } )
                ex2. HTML Tag Matching
                    - stack pair
                    push : <name>
                    pop : </name>
                ex3. Evaluating Arithmetic Expressions
                    - value stack : 값 저장
                    - operation stack : 연산 기호 저장
                    S[i]
                    X[j] <= X[i]
                ex4. Computing Spans

    5. Queue
        1) The Queue ADT
            (1) 특징
                - FIFO
            (2) Queue ADT
                1] Main Queue Operations
                    Q.enqueue(object)
                    Q.dequeue()
                2] Auxiliary Queue Operations
                    Q.first() ♣
                    Q.peek(index) ♣♣♣
                    len(Q)
                    is_empty(Q)
                    is_full(Q)
                3] Exceptions
                    EmptyQueueException ♣
        2) Queue Operations
            - Queue 설계에 따라 변화
            (1) Array-Based Queue
                - circular fashion ♣
                f : front element
                r : rear element
                N : array of size
            (2) Queue Operations ♣♣
                1] Algorithm size()
                    return (N-f+r) mod N
                2] Algorithm isEmpty()
                    return (f=r)
                3] Algorithm enqueue(o)
                    if size() == N - 1 then
                        throw FullQueueException
                    else
                        Q[r] <- o
                        r <- (r+1) mod N
            (3) Queue in Python : 강의자료 참조 ♣♣
        3) Application of Queues
            (1) Applications Ex
                1] Direct applications ♣
                    ex1. Waiting lists / CPU Scheduling / Disk Scheduling
                    ex2. Access to shared resources
                    ex3. Multiprogramming / Scheduling
                    ex4. Interrupts in real-time systems
                    ex5. Call Center
                2] Indirect applications
                    ex6. Auxiliary data structure for algorithms
                    ex7. Component of other data structures
            (2) Algorithm Ex ♣♣
                ex1. Round Robin Schedulers : circular queue
                ex2. Circular Queue : circular queue
            (3) Python : 강의자료 참조

    6. Linked List
        1) Singly linked list
            (1) 특징
                1] 구조 : 노드(head) -> 노드 -> 노드 -> ... -> 노드(tail) -> Null ♣
                    - 노드 : 원소 + next 주소
                    - 원소 : 데이터
                    - next 주소 : 다음 데이터 위치
                2] 비교
                    [1] 기존 list
                        - memory 뭉탱이 할당
                        - 용량 초과시 copy & paste
                    [2] Singly linked list
                        - 기존 list보다 memory 공간 2배 할당
                        - 필요할 때마다 node 만들어 사용
                    [3] Doubly linked list
                        - 기존 list보다 memory 공간 3배 할당
                        - 필요할 때마다 node 만들어 사용
                3] 시간 복잡도
                    - Space : O(n)
                    - Stack ADT : O(1)
            (2) 연산
                1] Inserting at Head
                    [1] 새 노드 할당
                    [2] 새 노드에 원소 삽입
                    [3] 새 노드 주소가 기존 Head 가르킴
                    [4] 새 노드를 Head로 지목
                    - 순서 지키지 않으면 link 잃어버릴 가능성 높음
                    - temp로 기억하고 있다면, 상관 없음
                1] Removing at Head
                    [1] 다음 노드를 Head로 지목
                    [2] Garbage Collector가 기존 Head 제거
                        - 메모리 공간에 떠돌아 다닐 수 있으므로 Garbage Collector로 제거
                2] Inserting at Tail
                    [1] 새 노드 할당
                    [2] 새 노드에 원소 삽입
                    [3] 새 노드 주소가 Null 가르킴
                    [4] 기존 Tail 노드 주소가 새 노드 가르킴
                    [5] 새 노드를 Tail로 지목
                2] Removing at Tail
                    [1] Head부터 Tail까지 가면서 previous 기억 ♣
                    [2] Tail 노드가 나오면 previous 노드의 주소가 Null 가리킴
                    [3] previous 노드를 Tail로 지목
                    [4] Garbage Collector가 기존 Tail 제거
                    - Singly linked list의 단점 ♣
                        Head부터 Tail까지 가면서 previous 기억해야함
                        이전노드가 Tail을 끊기 위해 다시 이전노드로 돌아가야하는데, Tail노드에서는 이전노드의 주소를 알 수 없기 때문이다.
                3] Inserting at Middle
                    [1] Head부터 Tail까지 가면서 previous 기억 ♣
                    [2] 새 노드 할당
                    [3] 새 노드에 원소 삽입
                    [4] 새 노드 주소가 Middle 노드 가리킴 ♣♣♣
                    [5] previous 노드 주소가 새 노드 가리킴
                3] Removing at Middle
                    [1] Head부터 Tail까지 가면서 previous 기억 ♣
                    [2] Middle 노드가 나오면 previous 주소가 Middle+1 노드 가리킴 ♣♣♣
                    [3] Garbage Collector가 기존 Middle 제거
            (3) 활용
                1] Linked list stack
                    - top element : first node ♣♣
                        Singly linked list의 단점으로 인해 first node를 빼는 용도로 사용 ♣♣♣
                    - Space : O(n)
                    - Stack ADT : O(1)
                2] Linked list queue
                    - front element : first node ♣♣♣
                        Singly linked list의 단점으로 인해 first node를 빼는 용도로 사용 ♣♣♣
                    - rear element : last node ♣♣♣
                    - Space : O(n)
                    - Stack ADT : O(1)

        2) Doubly linked list
            (1) 특징
                1] 구조 : header <-> 노드 <-> 노드 <-> 노드 <-> ... <-> trailer ♣
                    - 노드 : 이전 주소 + 원소 + 다음 주소
                    - previous 주소 : 이전 데이터 위치
                    - 원소 : 데이터
                    - next 주소 : 다음 데이터 위치
                2] 비교
                    [1] 기존 list
                        - memory 뭉탱이 할당
                        - 용량 초과시 copy & paste
                    [2] Singly linked list
                        - 기존 list보다 memory 공간 2배 할당
                        - 필요할 때마다 node 만들어 사용
                    [3] Doubly linked list
                        - 기존 list보다 memory 공간 3배 할당
                        - 필요할 때마다 node 만들어 사용
                3] 시간 복잡도
                    - Space : O(n)
                    - Stack ADT : O(1)
                    >> 매우 빠름 but 일반 list, Singly linked list보다 느림
            (2) 연산
                1] insertion
                    [1] 이전 노드의 next 주소가 새 노드 가리킴
                    [2] 다음 노드의 previous 주소가 새 노드 가리킴
                2] deletion
                    [1] 이전 노드의 next 주소가 삭제 다음 노드 가리킴
                    [2] 다음 노드의 previous 주소가 이전 노드 가리킴
                    [3] Garbage Collector가 기존 노드 제거
            (3) 활용
                1] Positional list : 이름으로 위치 나타냄 ♣♣♣
                    - 잘 사용하지 않는다
        3) 총정리
            (1) 일반 list
                - 메모리 공간 1배
            (2) singly linked list
                - 메모리 공간 2배
                - 역방향 불가능. 한쪽 방향 원소 조작 용이 ♣
                - head, middle, tail 노드에서 각기 다른 방식 연산 ♣♣♣
            (3) doubly linked list
                - 메모리 공간 3배
                - 역방향 가능. 양쪽 방향 원소 조작 용이 ♣
                - 모든 노드에서 동일한 방식 연산 ♣

    7. Tree
        1) 개요
            (1) 특징 ♣
                - 계층 구조의 추상적 모델 ♣♣♣
                - 각 노드 : 부모 관계
            (2) 예시 ♣
                ex1. 조직 차트
                ex2. 파일 시스템
                ex3. 프로그래밍 환경
            (3) 용어 ♣
                1] Root : 부모 없는 노드
                2] Internal node : 적어도 1개 자식 있는 노드(root도 Internal node이다) ♣♣♣
                3] External node : 자식 없는 노드

                1] Depth of a node : 조상의 개수 ♣♣♣
                2] Height of a node : 노드의 최대 Depth ♣♣♣

                1] subtree ♣

                - ancestors of a node : 부모, 조부모, 조조부모, ...
                - descendant of a node : 자식, 손자, 손손자, ...
            (4) 구현 방법 ♣♣♣
                1] list
                2] doubly linked list
        2) Tree ADT ♣♣
            (1) 포괄적 메소드(Generic methods)
                - Integer len()
                - Boolean is_empty()
                - Iterator position() ♣
                - Iterator iter() ♣
            (2) 접근자 메소드(Accessor methods)
                - Position root()
                - Position parent(p)
                - Iterator children(p) ♣
                - Integer num_children(p) ♣
            (3) 질문 메소드(Query methods)
                - Boolean is_leaf(p) ♣♣
                - Boolean is_root(p)
            (4) 업데이트 메소드(Update methods)
                - Element replace(p, o)
        3) Application of Trees
            (1) Tree Traversal ♣♣
                1] 특징
                    - 모든 노드 1번씩 방문
                2] 종류 ♣♣♣ 좀 어렵네
                    - subtree의 모음이라고 생각
                    [1] Preorder traversal : VLR(root -> left -> right)
                        - 특징 : root가 가장 먼저
                        ex. 구조화된 문서 출력 ♣♣♣
                    [2] Inorder traversal : LVR(left -> root -> right)
                        - 특징 : root가 중간
                    [3] Postorder traversal : LRV(left -> right -> root)
                        - 특징 : root가 마지막
                        ex. 폴더 내 파일 사용 공간 계산 ♣♣♣
                3] 구현 ♣♣
                    [1] Preorder Traversal ♣
                        Algorithm preOrder(v)
                            visit(v)
                            for each child w of v
                                preOrder(w)
                    [3] Postorder Traversal ♣
                        Algorithm postOrder(v)
                            for each child w of v
                                postOrder(w)
                            visit(v)
        4) 종류
            (2) Binary Trees ♣♣
                1] Proper Binary Trees 특징 ♣♣♣
                    [1] 각 node : 최대 2개 자식(ordered pair = left node, right node)
                    [2] e = i + 1
                    [2] n = 2e - 1 = i + e
                    [2] h >= log_2(e) ♣♣♣
                    [3] edge의 개수 : n - 1개
                        - root를 제외한 모든 node에 부모로 이어지는 edge 존재
                    - n : nodes의 개수
                    - e : external nodes의 개수
                    - i : internal nodes의 개수
                    - h : height
                2] 종류
                    [1] Binary tree : 일반적 tree
                    [2] Full binary tree : 모든 level에서 꽉찬 tree
                    [3] Complete binary tree : 마지막 level에서 조금 비어있는 tree ♣
                3] 예시 ♣
                    ex1. 산수(arithmetic expressions)
                        Internal node : 연산자
                        External node : 피연산자
                        ex. 2 x (a - 1) + (3 x b)
                    ex2. decision processes
                        Internal node : yes or no로 대답가능한 질문
                        External node : 선택 시 결과
                        ex. dining decision
                    ex3. searching
                4] 구현 ♣♣
                    [1] Inorder Traversal - Binary Tree ♣♣
                        Algorithm inOrder(v)
                            if v has a left child
                                inOrder(left(v))
                            visit(v)
                            if v has a right child
                                inOrder(right(v))
                    [2] Print Arithmetic Expressions(Inorder traversal) - Binary Tree ♣♣
                        Algorithm printExpression(v)
                            if v has a left child
                                print("(")
                                printExpression(left(v))
                            print(v.element())
                            if v has a right child
                                printExpression(right(v))
                                print(")")
                    [2] Print Arithmetic Expressions(recursive)(Postorder traversal) - Binary Tree ♣♣♣
                        Algorithm evalExpr(v)
                            if is_leaf(v)
                                return v.element()
                            else
                                x <- evalExpr(left(v))
                                y <- evalExpr(right(v))
                                o <- operator stored at v
                                return x o y
                    [3] Euler Tour Traversal - Binary Tree ♣♣
                        - 최대 3번 방문
                        1]] preorder : on the left ♣♣
                        2]] inorder : from below ♣♣
                        3]] postorder : on the right ♣♣
                        
                        1]] 자식 0개 node : 1번 방문
                        2]] 자식 1개 node : 2번 방문
                        3]] 자식 2개 node : 3번 방문
                5] 구현 방법 종류
                    [1] Linked Structure - Binary Tree(1개 노드 당 3개 공간) ♣♣♣
                        - 3가지 저장
                            데이터
                            부모 노드
                            자식 노드
                    [2] Linked Structure - Binary Tree(1개 노드 당 4개 공간) ♣♣♣
                        - 4가지 저장
                            데이터
                            부모 노드
                            왼쪽 자식 노드
                            오른쪽 자식 노드
                    [3] Array based Binary Tree ♣♣♣
                        - Full binary tree를 array based로 구현 : 효율성 높음
                        - 듬성듬성한 binary tree를 array based로 구현 : 효율성 낮음

                        - root node = 1
                        - parent node의 왼쪽 자식 = parent node x 2
                        - parent node의 오른쪽 자식 = parent node x 2 + 1

    8. Priority Queues
        1) 개요
            (1) 특징
                1] (key, value)쌍 item 저장
                2] key만 순서에 영향
            (2) 활용
                [1] Standby flyers
                [2] Auctions
                [3] Stock market
        2) The Priority Queue ADT
            1] Main Priority Queue Operations
                add(k, x) : key k, value x인 item 삽입
                remove_min() : key가 가장 작은 item 삭제
            2] Auxiliary Priority Queue Operations
                min() : 최소값인 key return
                len(P)
                is_empty()
        3) 예시
            - 강의자료 참조
        4) 연산
            1] unsorted array : dequeue 시 sort
                - enqueue() : O(1)
                - dequeue() : O(n)
            1] sorted array : enqueue 시 sort
                - enqueue() : O(n)
                - dequeue() : O(1)
            2] unsorted linked list : dequeue 시 sort
                - enqueue() : O(1)
                - dequeue() : O(n)
            2] sorted linked list : enqueue 시 sort
                - enqueue() : O(n)
                - dequeue() : O(1)
            3] heap ♣♣♣
                - enqueue() : O(logn)
                - dequeue() : O(logn)

                - n이 커질수록 진가 발휘
                - 동일한 성능 보장 in 실시간 작업

            1] unsorted array
                add : O(1)
                remove_min = min : O(n)
            1] sorted array
                add : O(n)
                remove_min = min : O(1)
        5) 활용
            1] PQ(Priority Queue) Sort
                [1] 알고리즘
                    1]] add
                    2]] remove_min
                [2] 종류
                    1]] Selection Sort in PQ : dequeue할 때 sort ♣♣♣
                        - insert : O(n)
                        - remove_min : n(n+1)/2 = O(n^2)

                    2]] Insertion Sort in PQ : enqueue할 때 sort ♣♣♣
                        - insert : n(n+1)/2 = O(n^2)
                        - remove_min : O(n)

                        Algorithm PQSort(S, C) ♣♣♣
                            input : sequence S, S의 원소에 대한 Comparator C
                            output : C에 따라 증가하는 순서로 정렬된 sequence S
                            while ~S.is_empty()
                                e <- S.remove_first()
                                P.add(e, null)
                            while ~P.is_empty()
                                e <- P.removeMin().key()
                                S.add_last(e)
                    3]] In-place Insertion Sort in PQ : 추가 메모리 사용x. swap
            2] Heap
                [1] 개념 : Complete binary tree 이용한 Priority Queue 구현 ♣♣♣
                [2] 특징
                    1]] Complete binary tree : 마지막 level에서 조금 비어있는 tree
                    2]] Heap order : root가 아닌 모든 internal node의 부자 관계는 key(v) >= key(parent(v)) ♣♣♣
                    3]] last node : 최대 depth의 최우측 node
                    4]] Heap의 height : O(logn) ♣♣♣
                        key : 2^i개 (i = 0, 1, ..., h-1 depth)
                            적어도 1개 (i = h depth)
                        2^h <= n
                        h <= logn
                [3] 알고리즘 ♣♣
                    1]] insertion
                        -> insertion node인 z 탐색
                        -> z에 k 저장
                        -> heap order property 복원 by upheap

                        - upheap
                            목적 : heap order property(internal node의 부자 관계 : key(v) >= key(parent(v))를 지키기 위함
                            시간복잡도 : O(logn)
                    2]] removal
                        -> root key와 last node w의 key를 swap
                        -> w 제거
                        -> heap order property 복원 by downheap
                        -> last node 업데이트 ♣♣

                        - down heap
                            목적 : heap order property(internal node의 부자 관계 : key(v) >= key(parent(v))를 지키기 위함
                            시간복잡도 : O(logn)
                        -  update last node ♣♣♣
                            -> 왼쪽에 부모 있으면 따라감. 왼쪽에 부모가 없을 때까지 따라감
                            -> 오른쪽에 부모 있으면 따라감. 오른쪽에 부모가 없을 때까지 따라감
                            -> 최대한 왼쪽에 있는 자식을 따라감. 왼쪽 자식이 없을 때까지 따라감

                            [[1]] 자료저장 시간복잡도 : O(logn) = logn + logn ♣
                            [[2]] 전체수행 시간복잡도 : O(n) ♣
                    3]] heap sort
                        시간복잡도
                            space : O(n)
                            add : O(logn)
                            len, is_empty, min : O(1) ♣♣♣
                            sort : O(nlogn) ♣♣♣
                    4]] merge two heaps
                        -> 2개 heap, 1개 key k 존재
                        -> root node에 k 넣고 2개 heap을 subtree로 해서 합쳐
                        -> heap order property 복원 by downheap ♣♣♣

                        - bottom up heap construction ♣♣♣
                            목적 : 2개 heap을 merge하기 위함
                            시간복잡도 : O(logn)
                                2^i - 1 keys를 가진 heap 2개를 2^(i+1) - 1의 keys를 가진 heap 1개로 병합
                [4] 구현 방법 종류
                    1]] 배열 기반 heap ♣♣
                        [[1]] 개념 : 배열을 이용 heap 구현
                        [[2]] 특징 ♣♣♣ Array Based Binary Tree와 인덱스를 다르게 매긴다
                            1]]] 인덱스
                                - node number
                                    왼쪽 자식 : 2i + 1
                                    오른쪽 자식 : 2i + 2
                                - add
                                    n + 1 인덱스에 원소 저장
                                - remove_min
                                    n 인덱스의 원소 삭제
                            2]]] 높은 성능
                [5] 예시 ♣♣♣
                    - 강의자료 참조


"""
