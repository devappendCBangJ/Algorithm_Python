class TreeNode():
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def Inorder(node):
	if node == None:
		return
	if node.left != None:
		print('(', end = ' ')
		Inorder(node.left)
	print(node.data, end = ' ')
	if node.right != None:
		Inorder(node.right)
		print(')', end = ' ')

node1 = TreeNode()
node1.data = "+" 

node2 = TreeNode()
node2.data = "x"
node1.left = node2

node3 = TreeNode()
node3.data = "x"
node1.right = node3

node4 = TreeNode()
node4.data = "2"
node2.left = node4

node5 = TreeNode()
node5.data = "-"
node2.right = node5

node6 = TreeNode()
node6.data = "a"
node5.left = node6

node7 = TreeNode()
node7.data = "1"
node5.right = node7

node8 = TreeNode()
node8.data = "3"
node3.left = node8

node9 = TreeNode()
node9.data = "b"
node3.right = node9

print('InOrder : ', end = ' ')
Inorder(node1)
print()
