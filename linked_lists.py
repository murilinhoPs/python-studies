from typing import *


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next: Node or None = None


class LinkedList:
    def __init__(self, head_node: Node):
        self.head = head_node

    def insert_at_beginning(self, data: str):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data: str):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (
            current_node.next
        ):  # passa por todos elementos da lista, quando um next dele for Null adiciona o novo node como next do current_node
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_index(self, data: str, index=0):
        return

    def print_LL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            if current_node.next != None:
                print(f'next -> {current_node.next.data}')
            current_node = current_node.next


initial_node = Node("murilo")
new_ll = LinkedList(initial_node)
new_ll.insert_at_end("murilinho")
new_ll.insert_at_beginning("muri")

new_ll.print_LL()
