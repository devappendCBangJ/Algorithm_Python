SIZE = 5
queue = ['A', 'B', 'C', 'D', 'E']
front = -1
rear = 4

def isQueueFull():
	global SIZE, front, rear
	if(rear == SIZE - 1):
		return True
	else:
		return False

print("check the full statement?", isQueueFull())
