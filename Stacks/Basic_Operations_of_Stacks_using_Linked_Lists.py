# WAP to implement basic operations of stack using linked list

# Class Definition for Linked List Node
class StackNode:
    # Function to initialise node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Definition for Linked List 
class Stack:

    # Function to initialise head
    def __init__(self):
        self.root = None

    # Function to check if the stack is empty
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
        
    # Function to add an item in the stack
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print("% d pushed to stack" % (data))

    # Function to delete an item from the stack
    def pop(self):
        if (self.isEmpty()):
            print("Stack Underflow")
            return
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        print("% d popped from stack" % (popped))

    # Function to return the top element of the stack without removing it
    def peek(self):
        if (self.isEmpty()):
            return
        return self.root.data


# Driver Code to test above functions
if __name__ == '__main__':

    # Define an empty Stack
    stack = Stack()

    # Function call to insert elements in the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Function call to delete an element from the stack
    stack.pop()

    # Function call to return the top element of the stack
    print("% d is the top element of the stack" % (stack.peek()))

    # Function call to check if the stack is empty
    print(stack.isEmpty())
