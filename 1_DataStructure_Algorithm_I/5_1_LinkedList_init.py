# 노드 Class
class Node():
	def __init__(self):
		self.data = None
		self.link = None

# 노드 생성 + 데이터 기입
node1 = Node()
node1.data = "Alice"

# 시각화
print(node1.data, end = ' ')
print(node1.data, end = '\n')
print(node1.data, end = '\r')
