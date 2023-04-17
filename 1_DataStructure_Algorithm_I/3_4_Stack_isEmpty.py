def isStackFull():
	global SIZE, stack, top

	if(top >= SIZE - 1): # 안전한 코드
		return True
	else:
		return False
		
def isStackEmpty():
	global SIZE, stack, top

	if(top <= -1): # 안전한 코드
		return True
	else:
		return False
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

def push(value):
	global SIZE, stack, top
	if (isStackFull() == True):
		print("Stack is Full!!")
		return
	else:
		top = top + 1
		stack[top] = value

print("check the empty statement?", isStackEmpty())
