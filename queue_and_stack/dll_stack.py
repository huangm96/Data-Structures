import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# A stack is a linear data structure in which elements can be inserted and deleted only from one side of the list, called the top.
# A stack follows the LIFO (Last In First Out) principle

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
