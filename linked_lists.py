from typing import *


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next: Node or None = None


class LinkedList:
    def __init__(self, head_node: Node):
        self.head = head_node

    def size(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0

    def insert_at_beginning(self, data: str):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: str):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current_node = self.head
        # passa por todos elementos da lista, quando um next dele for Null adiciona o novo node como next do current_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_index(self, data: str, target_index=0):
        if target_index == 0:
            print("insert_at_beginning")
            self.insert_at_beginning(data)
            return

        if target_index == self.size():
            print("insert_at_end")
            self.insert_at_end(data)
            return
        
        # passar pelos elementos da lista até encontrar o index desejado
        # ir somando no current_index++ até que ele seja engual o index atual, atualizar o current_node com o next dele toda vez que somar +1
        # achei o index certo!
        # criar o new_node, o next dele vai ser o current_node.next e o current_node.next = new_node
        current_index = 1  # starts at 1, if is 0 insert_at_beginning (up)
        current_node = self.head  # primeiro index (node)
        while current_node != None and current_index != target_index:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            print("index não existe")
            raise Exception("Index is out of bounds")
            return

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def print_LL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            if current_node.next != None:
                print(f"next -> {current_node.next.data}")
            current_node = current_node.next


initial_node = Node("murilo")
new_ll = LinkedList(initial_node)
new_ll.insert_at_end("murilinho")
new_ll.insert_at_beginning("muri")
print(new_ll.size())
new_ll.insert_at_index("djdjd", target_index=3)

new_ll.print_LL()
