class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*(self.maxsize + 1)
        # self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos//2
    def leftchild(self, pos):
        return 2 * pos
    def rightchild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def print(self):
        for i in range(self.maxsize):
            print(self.heap[i])

min_heap = MinHeap(15)
min_heap.print()