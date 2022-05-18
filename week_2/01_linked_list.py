class Node:
    def __init__(self, value):
        self.data = value
        self.next = None # 다음 노드 포인터


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None: # 다음 노드가 None 이면 마지막 노드에 도달
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None: # 마지막 노드에 도달 하기까지 print
            print(cur.data)
            cur = cur.next

    def get_node(self, index): # next 노드로 가는것을 index 만큼 해라
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value): # 몇번째, 무슨값
        new_node = value
        node = self.get_node(index -1)
        next_node = node.next
        node.next = new_node
        next_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6)
linked_list.print_all()