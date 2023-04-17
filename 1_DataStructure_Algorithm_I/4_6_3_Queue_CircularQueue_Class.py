# front : 첫 데이터 앞 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()과 isQueueEmpty()의 조건이 같아져버림

# front : 첫 데이터 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()와 isQueueEmpty()의 조건이 같아져버림

# -> 결국 똑같은 상황

class CircularQueue:
    def __init__(self, SIZE, queue, front, rear, count):
        self.SIZE = SIZE
        self.queue = queue
        self.front = front
        self.rear = rear
        self.count = count

    def isQueueFull(self):
        # if(front == rear):
        if(self.count == self.SIZE):
            return True
        else:
            return False

    def enQueue(self, data):
        if(self.isQueueFull()):
            print("Queue is Full ...")
            return None
        if(self.rear == self.SIZE-1):
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = data

        self.count += 1

    def isQueueEmpty(self):
        # if(front == rear):
        if(self.count == 0):
            return True
        else:
            return False

    def deQueue(self):
        if(self.isQueueEmpty()):
            print("Queue is empty ...")
            return None

        if(self.front == self.SIZE-1):
            self.front = 0
        else:
            self.front += 1

        self.data = self.queue[self.front]
        self.queue[self.front] = None

        self.count -= 1
        return self.data

queue1 = CircularQueue(5, ['A', None, None, None, None], -1, 0, 1)
# SIZE = 5
# count = 1
# queue = ['A', None, None, None, None]
# front = -1
# rear = 0

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡCircularQueue Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(4):
    for j in range(i):
        print("ㅡㅡㅡㅡㅡenQueue({})ㅡㅡㅡㅡㅡ".format(j))
        queue1.enQueue(j)
        print("front : {}, rear : {}".format(queue1.front, queue1.rear))
        print(queue1.queue)
    for j in range(i):
        print("ㅡㅡㅡㅡㅡdeQueueㅡㅡㅡㅡㅡ")
        queue1.deQueue()
        print("front : {}, rear : {}".format(queue1.front, queue1.rear))
        print(queue1.queue)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡisQueueFull Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(6):
    queue1.enQueue(1)
    print(queue1.queue)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡisQueueEmpty Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(6):
    queue1.deQueue()
    print(queue1.queue)