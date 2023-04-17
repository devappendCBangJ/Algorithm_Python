class HanoiStack:
	def __init__(self, SIZE, stack, top):
		self.SIZE = SIZE
		self.stack = stack
		self.top = top
		self.data = None
	def isStackFull(self):
		if (self.top >= self.SIZE - 1):  # 안전한 코드
			return True
		else:
			return False

	def isStackEmpty(self):
		if (self.top <= -1):  # 안전한 코드
			return True
		else:
			return False

	def push(self, value):
		if (self.isStackFull() == True):
			print("Stack is Full!!")
			return
		else:
			self.top = self.top + 1
			self.stack[self.top] = value

	def pop(self):
		if (self.isStackEmpty() == True):
			print("Stack is Empty!!")
			return None
		else:
			self.data = self.stack[self.top]
			self.stack[self.top] = None
			self.top = self.top - 1
			return self.data

SIZE = 5
stackA = ['1', '2', '3', '4', '5']
stackB = [None, None, None, None, None]
stackC = [None, None, None, None, None]
top = -1

HanoiStackA = HanoiStack(SIZE, stackA, 4)
HanoiStackB = HanoiStack(SIZE, stackB, top)
HanoiStackC = HanoiStack(SIZE, stackC, top)

def hanoi(_num, _from, _to, _other):
	if _num == 0:
		return
	hanoi(_num-1, _from, _other, _to)
	_to.push(_from.pop())
	print(HanoiStackA.stack)
	print(HanoiStackB.stack)
	print(HanoiStackC.stack)
	print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
	hanoi(_num-1, _other, _to, _from)

print(2**SIZE - 1, "회 움직임")
hanoi(SIZE, HanoiStackA, HanoiStackC, HanoiStackB)