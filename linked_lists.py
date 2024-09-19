from typing import *


#  https://www.geeksforgeeks.org/python-linked-list/

class Node:
    def __init__(self, data: str):
        self.data = data
        self.next: Node or None = None


class LinkedList:
    def __init__(self, head_node: Node = None):
        self.head = head_node

    def size(self):
        size = 0
        if self.head is None:
            return 0

        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

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
        # passa por todos elementos da lista, quando um next dele for Null adiciona o novo node como next do
        # current_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_index(self, data: str, target_index=0):
        if target_index == 0:
            print("insert_at_beginning")
            self.insert_at_beginning(data)
            return

        current_index = 0  # starts at 1, if is 0 insert_at_beginning (up)
        current_node = self.head  # first index (node)
        while current_node and current_index != target_index:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            print("index não existe")
            raise Exception("Index is out of bounds")

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    #  insert before, the node must know its next and its previouss
    def insert_after_node(self, node_data: str, new_data: str):
        current_node = self.head

        if current_node is None:
            print("lista vazia")
            return

        new_node = Node(new_data)
        if current_node.data == data:
            new_node.next = current_node.next
            current_node.next = new_value
            return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            print("esse elemento não existe")
            raise Exception("Element is None")

        current_node.data = new_value

    def update_index(self, new_value: str, target_index=0):
        if target_index == 0:
            self.head.data = new_value
            return

        current_index = 0
        current_node = self.head
        while current_node and current_index != target_index:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            print("index não existe")
            raise Exception("Index is out of bounds")

        current_node.data = new_value

    def update_node(self, data: str, new_value: str):
        current_node = self.head

        if current_node is None:
            print("lista vazia")
            return

        if current_node.data == data:
            self.head.data = new_value
            return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            print("esse elemento não existe")
            raise Exception("Element is None")

        current_node.data = new_value

    def remove_first(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last(self):
        current_node = self.head
        if current_node is None:
            return

        while current_node.next.next:
            current_node = current_node.next

        # vai remover o proximo dele, que é realmente oo último elemento
        current_node.next = None

    def remove_at_index(self, target_index=0):
        if self.head is None:
            print("sem elementos para remover")
            return

        if target_index == 0:
            print("remove_first")
            self.remove_first()
            return

        current_index = 1  # starts at 1, if is 0 remove_first (up)
        current_node = self.head  # first index (node)
        while current_node and current_index < target_index:
            current_index += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("index não existe")
            raise Exception("Index is out of bounds")

        current_node.next = (
            current_node.next.next
        )  # o proximo é igual o proximo do proximo, assim removendo o next atual

    def remove_node(self, data: str):
        current_node = self.head

        if current_node is None:
            print("sem elementos para remover")
            return

        if current_node.data == data:
            print("remove_first")
            self.remove_first()
            return

        while current_node and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            print("elemento não existe")
            raise Exception("Element is None")

        # o current.proximo é igual o proximo dele mesmo, assim removendo o next atual
        current_node.next = current_node.next.next

    def print_ll(self):
        current_node = self.head
        while current_node:  # already checks if is not None
            print(f"node: {current_node.data}")
            if current_node.next:
                print(f"next -> {current_node.next.data}")
            current_node = current_node.next


initial_node = Node("murilo")
new_ll = LinkedList(initial_node)
new_ll.insert_at_end("murilinho")
new_ll.insert_at_beginning("muri")
new_ll.insert_at_index("jorge", target_index=2)
print(f"size: {new_ll.size()}")
print("")

new_ll.print_ll()
new_ll.update_index("jorge jr", 3)  # atualizar o ultimo elemento
new_ll.update_node("murilinho", "murilinhops")
print("")

new_ll.print_ll()
new_ll.remove_at_index(3)  # remove last element
# new_ll.remove_last()
print("")

new_ll.print_ll()
