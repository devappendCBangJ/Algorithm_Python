SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

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

print("check the empty statement?", isQueueEmpty())
