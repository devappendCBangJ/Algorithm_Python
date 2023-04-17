# front : 첫 데이터 앞 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()과 isQueueEmpty()의 조건이 같아져버림

# front : 첫 데이터 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()와 isQueueEmpty()의 조건이 같아져버림

# -> 결국 똑같은 상황

def isQueueFull():
    global SIZE, queue, front, rear
    # if(front == rear):
    if(count == SIZE):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear, count
    if(isQueueFull()):
        print("Queue is Full ...")
        return None
    if(rear == SIZE-1):
        rear = 0
    else:
        rear += 1
    queue[rear] = data

    count += 1

def isQueueEmpty():
    global SIZE, queue, front, rear
    # if(front == rear):
    if(count == 0):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear, count
    if(isQueueEmpty()):
        print("Queue is empty ...")
        return None

    if(front == SIZE-1):
        front = 0
    else:
        front += 1

    data = queue[front]
    queue[front] = None

    count -= 1
    return data

SIZE = 5
count = 1
queue = ['A', None, None, None, None]
front = -1
rear = 0

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡCircularQueue Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(4):
    for j in range(i):
        print("ㅡㅡㅡㅡㅡenQueue({})ㅡㅡㅡㅡㅡ".format(j))
        enQueue(j)
        print("front : {}, rear : {}".format(front, rear))
        print(queue)
    for j in range(i):
        print("ㅡㅡㅡㅡㅡdeQueueㅡㅡㅡㅡㅡ")
        deQueue()
        print("front : {}, rear : {}".format(front, rear))
        print(queue)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡisQueueFull Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(6):
    enQueue(1)
    print(queue)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡisQueueEmpty Testㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(6):
    deQueue()
    print(queue)