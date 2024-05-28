# WAP to implement basic operations of Queue using Array

# Class Queue to represent a queue
class Queue:

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Function to check if the Queue is Full
    def isFull(self):
        return self.size == self.capacity
    
    # Function to check if the Queue is Empty
    def isEmpty(self):
        return self.size == 0
    
    # Function to add an item in the Queue
    def EnQueue(self, item):
        if self.isFull():
            print("Overflow Condition")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    # Function to remove an item from the queue
    def DeQueue(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    # Function to get front of the queue
    def que_front(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        print("Front item is ", self.Q[self.front])

    # Function to get rear of the queue
    def que_rear(self):
        if self.isEmpty():
            print("Underflow Condition")
            return
        print("Rear item is ", self.Q[self.rear])

    
# Driver code to test the above functions
if __name__ == '__main__':

    queue = Queue(30)

    # Funtion call to add items in the queue
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)

    # Function call to remove an item from the queue
    queue.DeQueue()

    # Function call to get the front of the queue
    queue.que_front()

    # Function call to get the rear of the queue
    queue.que_rear()