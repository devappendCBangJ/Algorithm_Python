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
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def heapDown(self, pos):
        if not self.isLeaf(pos):
            if(self.heap[pos] > self.heap[self.leftchild(pos)] or
                self.heap[pos] > self.heap[self.rightchild(pos)]):
                if(self.heap[self.leftchild(pos)] < self.heap[self.rightchild(pos)]):
                    self.swap(pos, self.leftchild(pos))
                    self.heapDown(self.leftchild(pos))
                else:
                    self.swap(pos. self.rightchild(pos))
                    self.heapDown(self.rightchild(pos))
    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]

        self.size -= 1
        self.heapDown(self.front)
        self.heap[self.size + 1] = 0

        return popped

    def print(self):
        for i in range(1, (self.size//2) + 1):
            print("parent[" + str(i) + "]: " + str(self.heap[i]) +
                  " / leftchild[" + str(2 * i) + "]: " + str(self.heap[2 * i]) +
                  " / rightchild[" + str(2 * i + 1) + "]: " + str(self.heap[2 * i + 1]))

min_heap = MinHeap(15)
min_heap.print()

min_heap.insert(5)
min_heap.print()

min_heap.insert(3)
min_heap.print()

min_heap.insert(17)
min_heap.print()

min_heap.insert(10)
min_heap.print()

min_heap.insert(84)
min_heap.print()

print("The min value is " + str(min_heap.remove()))
print("ㅡㅡㅡㅡㅡ min ㅡㅡㅡㅡㅡ")
min_heap.print()

print("The min value is " + str(min_heap.remove()))
print("ㅡㅡㅡㅡㅡ min ㅡㅡㅡㅡㅡ")
min_heap.print()

print("The min value is " + str(min_heap.remove()))
print("ㅡㅡㅡㅡㅡ min ㅡㅡㅡㅡㅡ")
min_heap.print()