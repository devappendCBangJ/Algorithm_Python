# 노드 Class
class Node():
	def __init__(self):
		self.data = None
		self.link = None

# 노드 생성 + 데이터 기입 + 링크 연결
node1 = Node()
node1.data = 30

node2 = Node()
node2.data = 40
node1.link = node2

node3 = Node()
node3.data = 50
node2.link = node3

node4 = Node()
node4.data = 60
node3.link = node4

node5 = Node()
node5.data = None
node4.link = node5
