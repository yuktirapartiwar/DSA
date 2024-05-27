# WAP a program to reverse a given linked list using
# 1. Iterative Method
# 2. Recursion Method

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

    # Function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Function to reverse Linked List using Iterative Method
    def reverseIterativeMethod(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to reverse Linked List using Recursion Method
    def reverseRecursionMethod(self, head):
        if head is None or head.next is None:
            return head
        
        rest = self.reverseRecursionMethod(head.next)

        head.next.next = head
        head.next = None

        return rest


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

    # Print Reverse of Linked List using Iterative Method
    print("\n\nReverse of Linked List using Iterative Method:")
    print("Given Linked List: ")
    linkedlist.printList()
    linkedlist.reverseIterativeMethod()
    print("\nReversed Linked List: ")
    linkedlist.printList()

    # Print Reverse of Linked List using Recursion Method
    print("\n\n\nReverse of Linked List using Recursion Method:")
    print("Given Linked List: ")
    linkedlist.printList()
    linkedlist.head = linkedlist.reverseRecursionMethod(linkedlist.head)
    print("\nReversed Linked List: ")
    linkedlist.printList()
