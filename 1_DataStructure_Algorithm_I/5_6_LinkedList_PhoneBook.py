# 노드 Class
class Node():
    def __init__(self):
        self.data_name = None
        self.data_num = None
        self.link = None

# Traveling + print (특정 노드부터)
def printNodes(start):
    current = start

    # Traveling + print
    if current == None:
        return
    print(current.data_name, end = ' ')
    while(current.link != None):
        current = current.link
        print(current.data_name, end = ' ')
    print()

# 노드 insert
def insertNode(findData, insertData):
    global head, current, pre

    # 첫 노드 insert
    if head.data_name == findData:
        node = Node()
        node.data_name = insertData[0]
        node.data_num = insertData[1]
        node.link = head
        head = node
        return
    current = head

    # 중간 노드 insert
    while current.link !=None:
        pre = current	# 이전 노드 기억
        current = current.link
        if current.data == findData:
            node = Node()
            node.data_name = insertData[0]
            node.data_num = insertData[1]
            node.link = current
            pre.link = node
            return

    # 마지막 노드 insert
    node = Node()
    node.data_name = insertData[0]
    node.data_num = insertData[1]
    current.link = node

# 노드 delete
def deleteNode(deleteData):
    global head, current, pre

    # 첫 노드 delete
    if head.data_name == deleteData:
        current = head
        head = head.link
        del(current)
        return
    current = head

    # 중간 노드 delete
    while current.link !=None:
        pre = current	# 이전 노드 기억
        current = current.link
        if current.data_name == deleteData:
            pre.link = current.link
            del(current)
            return

# 데이터 초기화
head, current, pre = None, None, None
dataName = [["Alice", "010-111-1111"], ["Bob", "010-222-2222"], ["Oracle", "010-333-3333"]]

if __name__ == "__main__":
    # 첫 노드. 생성 + 데이터 기입 + 링크 연결
    node = Node()
    node.data_name = dataName[0][0]
    node.data_num = dataName[0][1]
    head = node

    insertNode("Alice", dataName[0])
    printNodes(head)

    insertNode("Alice", dataName[1])
    printNodes(head)

    deleteNode("Alice")
    printNodes(head)

    insertNode("Bob", dataName[2])
    printNodes(head)