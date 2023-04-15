class TreeNode():
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode()
node1.data = "Alice"

node2 = TreeNode()
node2.data = "Bob"
node1.left = node2

node3 = TreeNode()
node3.data = "Oracle"
node1.right = node3

node4 = TreeNode()
node4.data = "James"
node2.left = node4

node5 = TreeNode()
node5.data = "Richard"
node2.right = node5

node6 = TreeNode()
node6.data = "Edward"
node3.left = node6

def Preorder(node):
	if node == None:
		return
	print(node.data, end = '->')
	Preorder(node.left)
	Preorder(node.right)
def Inorder(node):
	if node == None:
		return
	Preorder(node.left)
	print(node.data, end = '->')
	Preorder(node.right)
def Postorder(node):
	if node == None:
		return
	Preorder(node.left)
	Preorder(node.right)
	print(node.data, end = '->')

print('PreOrder : ', end = ' ')
Preorder(node1)
print('end')

print('InOrder : ', end = ' ')
Inorder(node1)
print('end')

print('PostOrder : ', end = ' ')
Postorder(node1)
print('end')
