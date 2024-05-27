# WAP to delete a node in the given Linked List from the following positions:
# 1. Beginning of the Linked List
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

    # Function to delete a node from the beginning of the linked list
    def deleteFromBegginning(self):
        self.head = self.head.next
        return self.head

    # Function to delete a node from a given position
    def deleteFromMiddle(self, position):
        temp = self.head
        prev = self.head
        for i in range (0, position):
            if i == 0 and position == 1:
                self.head = self.head.next

            else:
                if i == position-1 and temp is not None:
                    prev.next = temp.next

                else:
                    prev = temp
                    if prev is None:
                        break
                    temp = temp.next

        return self.head 
    
    # Function to delete a node from the end of the linked list
    def deleteFromEnd(self):
        last = self.head
        while(last.next):
            prev = last
            last = last.next        
        prev.next = None

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

    # Deletion from the beginning of the linked list
    print(f"\n\nDelete a node from beginning of the linked list:")
    print("Given Linked List: ")
    linkedlist.printList()
    linkedlist.deleteFromBegginning()
    print("\nNew Linked List: ")
    linkedlist.printList()
    
    # Deletion from a given position
    position = 2
    print(f"\n\nDelete a node from {position} position of the linked list:")
    print("Given Linked List: ")
    linkedlist.printList()
    linkedlist.deleteFromMiddle(position)
    print("\nNew Linked List: ")
    linkedlist.printList()

    # Deletion from the end of the linked list
    print(f"\n\nDelete a node from end of the linked list:")
    print("Given Linked List: ")
    linkedlist.printList()
    linkedlist.deleteFromEnd()
    print("\nNew Linked List: ")
    linkedlist.printList()

    