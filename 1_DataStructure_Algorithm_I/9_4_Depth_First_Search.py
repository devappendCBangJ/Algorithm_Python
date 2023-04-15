# Graph 정의
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# Global 변수
G1 = None
stack = []
visitedArr = []

# Graph 생성
G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

# Graph 시각화
print("## G1 undirected graph ##")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

# 초기화
current = 0
stack.append(current)
visitedArr.append(current)

while(len(stack) != 0):
    next = None

    # current와 연결된 vertex 확인
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedArr:            # visited vertex : pass
                pass
            else:                               # not visited vertex : 해당 vertex 저장
                next = vertex
                break

    # current와 연결된 not visited vertex확인
    if next != None:                            # current와 연결된 not visited vertex 존재o : 해당 vertex를 current로 하여 재탐색
        current = next
        stack.append(current)
        visitedArr.append(current)
    else:                                       # current와 연결된 not visited vertex 존재x : stack의 가장 마지막값 pop, 이 값을 current로 하여 재탐색
        current = stack.pop()

print('Traveling order -->', end = '')
for i in visitedArr:
    print(chr(ord('A')+i), end='    ')