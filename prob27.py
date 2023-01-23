"""Problem Statement on how to find middle element of linked list in python
In this problem, we are given a singly linked list. We have to find the middle of the linked list in a single traversal.
Suppose the given list is 5 → 10 → 15 → 4 → 8. The middle of the list will be 15."""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)

list1 = LinkedList()
list1.push(8)
list1.push(4)
list1.push(15)
list1.push(10)
list1.push(5)
list1.printMiddle()