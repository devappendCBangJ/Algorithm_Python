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

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
    def insert(self, ele):
        if(self.size >= self.maxsize):
            return
        self.size += 1
        self.heap[self.size] = ele

        print("insert : " + str(ele))

        cur = self.size
        while(self.heap[cur] < self.heap[self.parent(cur)]):
            self.swap(self.heap[cur], self.heap[self.parent(cur)])
            cur = self.parent(cur)

    def print(self):
        for i in range(1, (self.size//2) + 1):
            print("parent[" + str(i) + "]" + str(self.heap[i]) +
                  " / leftchild[" + str(2 * i) + "]" + str(self.heap[2 * i]) +
                  " / rightchild[" + str(2 * i + 1) + "]" + str(self.heap[2 * i + 1]))

min_heap = MinHeap(15)
min_heap.print()

min_heap.insert(5)
min_heap.print()

min_heap.insert(5)
min_heap.print()

min_heap.insert(17)
min_heap.print()

min_heap.insert(10)
min_heap.print()

min_heap.insert(84)
min_heap.print()