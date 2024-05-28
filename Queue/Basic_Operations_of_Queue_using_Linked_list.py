# WAP to implement basic operations of Queue using Linked List

class QNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None

    # Function to check if the Queue is Empty
    def isEmpty(self):
        return self.front == None
    
    # Function to add an item in the Queue
    def EnQueue(self, item):
        temp = QNode(item)

        if self.rear == None:
            self.front = self.rear = temp
            print("% s enqueued to queue" % str(item))
            return
        self.rear.next = temp
        self.rear = temp
        print("% s enqueued to queue" % str(item))

    # Function to remove an item from the queue
    def DeQueue(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        temp = self.front
        print("% s dequeued from queue" % str(temp.data))
        self.front = temp.next

        if(self.front == None):
            self.rear = None

    # Function to get front of the queue
    def que_front(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        print("Front item is ", self.front.data)

    # Function to get rear of the queue
    def que_rear(self):
        if self.isEmpty():
            print("Under Condition")
            return
        print("Rear item is ", self.rear.data)


# Driver Code
if __name__ == '__main__':

    q = Queue()
    
    # Function call to add items in the queue
    q.EnQueue(10)
    q.EnQueue(20)
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)

    # Function call to remove items from the queue
    q.DeQueue()
    q.DeQueue()

    # Function call to get the front of the queue
    q.que_front()

    # Function call to get the rear of the queue
    q.que_rear()