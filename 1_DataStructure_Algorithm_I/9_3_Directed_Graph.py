# Graph 정의
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# Global 변수
G1, G3 = None, None

# Graph 생성
G3 = Graph(4)
G3.graph[0][2] = 1
G3.graph[1][0] = 1; G3.graph[1][2] = 1
G3.graph[2][3] = 1

print("## G3 directed graph ##")
for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end = ' ')
    print()