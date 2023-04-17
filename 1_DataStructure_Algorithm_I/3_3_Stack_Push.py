def isStackFull():
	global SIZE, stack, top

	if(top >= SIZE - 1): # 안전한 코드
		return True
	else:
		return False
		
def push(value):
	global SIZE, stack, top
	if (isStackFull() == True):
		print("Error")
	else:
		top = top + 1
		stack[top] = value

SIZE = 5
stack = ['A', 'B', 'C', 'D', None]
top = 3

print(stack)
push('E')
print(stack)
push('F')
