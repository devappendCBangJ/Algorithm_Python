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

def push(value):
	global SIZE, stack, top
	if (isStackFull() == True):
		print("Stack is Full!!")
		return
	else:
		top = top + 1
		stack[top] = value

def pop():
	global SIZE, stack, top
	if(isStackEmpty() == True):
		print("Stack is Empty!!")
		return None
	else:
		data = stack[top]
		stack[top] = None
		top = top - 1
		return data

SIZE = 5
stack = ['A', None, None, None, None]
top = 0

print(stack)
retData = pop()
print("return data : ", retData)
print(stack)
retData = pop()
