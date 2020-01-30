import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # 
    def insert(self, value):
        if value < self.value :
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else :
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.left is None or self.right is None:
            return False
        elif target > self.value:
            return self.right.contains(target)
        elif target < self.value:
            return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node.left:
            print(node.value)
        if node.left:
            node.left.in_order_print(node.left)
            print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.enqueue(node)
        while storage.len() > 0:
            new_node = storage.dequeue()
            print(new_node.value)
            if new_node.left:
                storage.enqueue(new_node.left)
            if new_node.right:
                storage.enqueue(new_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)
        while storage.len() > 0:
            new_node = storage.pop()
            print(new_node.value)
            if new_node.left:
                storage.push(new_node.left)
            if new_node.right:
                storage.push(new_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
