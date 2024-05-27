# WAP to search an element in a linked list using - 
# 1. O(N) Extra Space - Vector
# 2. Iterative Approach
# 3. Recursive Approach

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

    # Funtion to search key using a vector
    def searchVectorApproach(self, key):
        temp = self.head
        v = []
        while(temp):
            v.append(temp.data)
            temp = temp.next

        if key in v:
            print("Yes")
        else:
            print("No")

    # Function to search key using iterative approach
    def searchIterativeApproach(self, key):
        current = self.head

        while current != None:
            if current.data == key:
                print("Yes")
                return
            current = current.next
        
        print("No")
        return
    
    # Function to search key using recursive approach
    def searchRecursiveApproach(self, linkedlist, key):
        if linkedlist is None:
            print ("No")
            return
        
        if(linkedlist.data == key):
            print ("Yes")
            return
        
        return self.searchRecursiveApproach(linkedlist.next, key)




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

    # Key to search in linked list
    key = 21

    # Function call to search key using vector
    print(f"Search for {key} using Vector: ")
    linkedlist.searchVectorApproach(key)

    # Function call to search key using iterative approach
    print(f"Search for {key} using Iterative Approach: ")
    linkedlist.searchIterativeApproach(key)

    # Function call to search key using recursive approach
    print(f"Search for {key} using Recursive Approach: ")
    linkedlist.searchRecursiveApproach(linkedlist.head, key)

