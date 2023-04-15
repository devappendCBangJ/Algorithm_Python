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
    print(current.data_name, end=' / ')
    print(current.data_num, end=' // ')
    while (current.link != None):
        current = current.link
        print(current.data_name, end=' / ')
        print(current.data_num, end=' // ')
    print()

# 노드 insert
def insertNode(insertData):
    global head, tail, current, pre

    # insert 노드 생성
    node = Node()
    node.data_name = insertData[0]
    node.data_num = insertData[1]

    # 첫 노드면 link로 연결x
    if (head == None):
        head = node
        return

    # 첫 노드 아니면 link로 연결
    else:
        current = head
        while current.link != None:
            current = current.link
        current.link = node


# 노드 delete
def deleteNode(deleteData):
    global head, current, pre

    # 첫 노드 delete
    if head.data_name == deleteData:
        current = head
        head = head.link
        del (current)
        return
    current = head

    # 중간 노드 delete
    while current.link != None:
        pre = current  # 이전 노드 기억
        current = current.link
        if current.data_name == deleteData:
            pre.link = current.link
            del (current)
            return


# 데이터 초기화
head, current, pre, tail = None, None, None, None
dataName = [["Alice", "010-111-1111"], ["Bob", "010-222-2222"], ["Oracle", "010-333-3333"]]

if __name__ == "__main__":
    insertNode(dataName[0])
    printNodes(head)

    insertNode(dataName[1])
    printNodes(head)

    deleteNode("Alice")
    printNodes(head)

    insertNode(dataName[2])
    printNodes(head)