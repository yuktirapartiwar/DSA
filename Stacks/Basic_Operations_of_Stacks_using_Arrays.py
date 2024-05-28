# WAP to implement basic operations of stack using array

from sys import maxsize

# Function to create a stack
def createStack():
    stack = []
    return stack

# Function to add an item in stack
def push(stack, item):
    stack.append(item)
    print("% d pushed to the stack" % (item))

# Function to check if the stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Function to delete an item from the stack
def pop(stack):
    if(isEmpty(stack)):
        print("Stack Underflow")
        return
    print("% d popped from stack" % stack.pop())

# Function to return the top element from the stack without removing it
def peek(stack):
    if(isEmpty(stack)):
        return
    return stack[-1]

# Function to return the length of the stack
def length(stack):
    return len(stack)

# Function to print the elements of the stack
def printStack(stack):
    print(stack)


# Driver program to test above functions
if __name__ == '__main__':

    # Function call to create a stack
    stack = createStack()

    # Function call to insert elements in the stack
    push(stack, 10)
    push(stack, 20)
    push(stack, 30)

    # Function call to delete an element from the stack
    pop(stack)

    # Function call to return the top element of the stack
    print("Top element of the stack is: ", peek(stack))

    # Function call to check if the stack is empty
    if isEmpty(stack):
        print("Stack is Empty")
    else:
        print("Stack is not Empty")

    # Function call to print the length of the stack
    print("Length of the Stack: " + str(length(stack)))

    # Function call to print the elements of the stack
    print("Stack: ")
    printStack(stack)