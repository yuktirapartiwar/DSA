# WAP to count number of nodes in a given singly linked list using -
# 1. Iterative Approach
# 2. Recursive Approach

# Class Definition for Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Definition for Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node at the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to count number of nodes using iterative approach
    def countIterativeApproach(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    # Function to count number of nodes using recursive approach
    def countRecursiveApproach(self, node, count = 0):
        if (not node):
            return count
        else:
            return self.countRecursiveApproach(node.next, count+1)

# Driver Code
if __name__ == '__main__':
    # Define an empty Linked List
    linkedlist = LinkedList()

    # Construct Linked List using Push()
    linkedlist.push(8)
    linkedlist.push(10)
    linkedlist.push(30)
    linkedlist.push(21)
    linkedlist.push(11)
    linkedlist.push(14)

    # Function call to Count Nodes using Iterative Approach
    print("Count of Nodes using Iterative Approach: ", linkedlist.countIterativeApproach())

    # Function call to Count Nodes using Recursive Approach
    print("Count of Nodes using Recursive Approach: ", linkedlist.countRecursiveApproach(linkedlist.head))