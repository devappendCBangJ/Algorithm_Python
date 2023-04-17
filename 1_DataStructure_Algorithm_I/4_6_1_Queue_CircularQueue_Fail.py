# front : 첫 데이터 앞 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()과 isQueueEmpty()의 조건이 같아져버림

# front : 첫 데이터 인덱스
# rear : 마지막 데이터 인덱스
# -> isQueueFull()와 isQueueEmpty()의 조건이 달라지므로 사용가능

def isQueueFull():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("Queue is Full ...")
        return None
    if(rear == SIZE-1):
        rear = 0
    else:
        rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("Queue is empty ...")
        return None

    if(front == SIZE-1):
        front = 0
    else:
        front += 1

    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ['A', None, None, None, None]
front = -1
rear = 0

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