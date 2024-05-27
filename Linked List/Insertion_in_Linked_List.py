# WAP to insert a new node in the given Linked List at the following positions:
# 1. At the front of the Linked List
# 2. After a given node
# 3. At the end of the linked list

# Class Definition for Linked List Node
class Node:
    # Function to initialise node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Definition for Linked List 
class LinkedList:

    # Function to initialise head
    def __init__(self):
        self.head = None

    # Funciton to insert a node at the front of the linked list
    def insertAtFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to find a note with given data
    def findNode(self, data):
        prev_node = self.head
        while prev_node is not None:
            if prev_node.data == data:
                return prev_node
            prev_node = prev_node.next
        return None

    # Function to insert a node after a given previous node
    def insertAfterNode(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node cannot be null.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Function to insert a node at the end of the linked list
    def insertAtLast(self, new_data):
        new_node = Node(new_data)
        new_node.data = new_data

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    # Function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# Driver Code
if __name__ == '__main__':
    linkedlist = LinkedList ()
    linkedlist.insertAtFront(6)
    linkedlist.insertAtFront(8)
    linkedlist.insertAtLast(9)
    linkedlist.insertAfterNode(linkedlist.findNode(6), 5)
    linkedlist.printList()
