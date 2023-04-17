SIZE = 5
queue = ['A', None, None, None, None]
front = -1
rear = 0

def isQueueFull():
	global SIZE, front, rear
	if(rear == SIZE - 1):
		return True
	else:
		return False

def isQueueEmpty():
	global SIZE, front, rear
	if(rear == -1):
		return True
	else:
		return False

def enQueue(value):
	global rear, front, queue, SIZE
	if(isQueueFull()):
		print('Queue is Full!')
		return None
	else:
		rear += 1
		queue[rear] = value

def deQueue():
	global rear, front, queue, SIZE
	if(isQueueEmpty()):
		print('Queue is Empty!')
		return None
	else:
		front += 1
		data = queue[front]
		queue[front] = None
		return data

print(queue)
retData = deQueue()
print("return data ", retData)
print(queue)
retData = deQueue()
