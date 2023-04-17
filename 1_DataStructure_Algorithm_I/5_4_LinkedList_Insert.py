# 노드 Class
class Node():
	def __init__(self):
		self.data = None
		self.link = None

# Traveling + print (특정 노드부터)
def printNodes(start):
	current = start

	# Traveling + print
	if current == None:
		return
	print(current.data, end = ' ')
	while(current.link != None):
		current = current.link
		print(current.data, end = ' ')
	print()

# 노드 insert
def insertNode(findData, insertData):
	global memory, head, current, pre

	# 첫 노드 insert
	if head.data == findData:
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	# 중간 노드 insert
	current = head
	while current.link !=None:
		pre = current	# 이전 노드 기억
		current = current.link
		if current.data == findData:
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	# 마지막 노드 insert
	node = Node()
	node.data = insertData
	current.link = node

# 데이터 초기화
memory = []
head, current, pre = None, None, None
dataArray = ["Alice", "Bob", "Donald", "Richard", "James"]

if __name__ == "__main__":
	# 첫 노드. 생성 + 데이터 기입 + 링크 연결
	node = Node()
	node.data = dataArray[0]
	head = node
	memory.append(node)

	# 남은 노드들. 생성 + 데이터 기입 + 링크 연결
	for data in dataArray[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.link = node	# 이전 노드 기억
		memory.append(node)

	printNodes(head)

	insertNode("Alice", "George")
	printNodes(head)

	insertNode("Bob", "Edward")
	printNodes(head)

	insertNode("Donald", "Michael")
	printNodes(head)