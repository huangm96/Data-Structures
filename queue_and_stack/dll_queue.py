import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList




# A queue is a linear data structure in which elements can be inserted only from one side of the list called rear,
# and the elements can be deleted only from the other side called the front.
# The queue data structure follows the FIFO (First In First Out) principle
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_head()
        

    def len(self):
        return self.size
