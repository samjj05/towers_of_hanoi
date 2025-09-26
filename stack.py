# importing Node for use in Stack
from node import Node

# Stack class

class Stack:
    # name attribute is used to differentiate left, middle and right Stack, all initially empty
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.top = None
    
    # adds a node to the top of the Stack
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
            self.size += 1
            return
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    # returns top node value, prints message if Stack is empty
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        return self.top.value
    
    # removes the top node, returns the value, prints message if Stack is empty
    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        value_removed = self.top.value
        if self.size == 1:
            self.top = None
            self.size = 0
            return value_removed
        self.top = self.top.next
        self.size -= 1
        return value_removed
    
    # returns True/False if stack is empty or not
    def is_empty(self):
        return self.size == 0

    # prints all values in order BACKWARDS, uses a list to do this to replicate seeing the disks visually
    def print_items(self):
        items = []
        current = self.top
        while current:
            items.append(current.value)
            current = current.next
        items.reverse()
        print(f"{self.name} Stack: {items}")
        

