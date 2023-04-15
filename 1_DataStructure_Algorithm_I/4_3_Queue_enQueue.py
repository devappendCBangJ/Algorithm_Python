SIZE = 5
queue = ['A', 'B', 'C', 'D', None]
front = -1
rear = 3

def isQueueFull():
	global SIZE, front, rear
	if(rear == SIZE - 1):
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

print(queue)
enQueue('E')
print(queue)
enQueue('F')
