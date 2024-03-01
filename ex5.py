#circular queue for arrays
class CircularQueueArray:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0 
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self._capacity
    
    def enqueue(self, value):
        if not self.isFull():
            self._data[self.tail] = value
            self.tail = (self.tail + 1) % self._capacity
            self.size += 1
            print(f"Enqueued {value} to the queue")
        else:
            print("Enqueue None")

    def dequeue(self):
        if not self.isEmpty():
            value = self._data[self.head]
            self.head = (self.head + 1) % self._capacity
            self.size -= 1
            print(f"Dequeued {value} from the queue")
        else:
            print("Dequeue None")
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty. Unable to peek item.")
            return None
        else:
            print("Peek None")
            value = self._data[self.head]
            print(f"Peeked {value} from the queue")
            return value
            
    
    def display(self):
        if not self.isEmpty():
            print("Queue: ", end="")
            for i in range(self.size):
                print(self._data[(self.head + i) % self._capacity], end=" ")
            print()
        else:
            print("Queue is empty")

#circualr queue for linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class CircularQueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Enqueued {value} to the queue")

    def dequeue(self):
        if not self.isEmpty():
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            print(f"Dequeued {value} from the queue")
        else:
            print("Dequeue None")
    
    def peek(self):
        if not self.isEmpty():
            value = self.head.value
            print(f"Peeked {value} from the queue")
            return value
        else:
            print("Peek None")
            return None
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


#used chatgpt
# Test operations
operations = [
    ("dequeue", None),
    ("peek", None),
    ("enqueue", 1),
    ("enqueue", 2),
    ("enqueue", 3),
    ("peek", None),
    ("enqueue", 4),
    ("enqueue", 5),
    ("enqueue", 6),
    ("enqueue", 7),
    ("enqueue", 8),
    ("enqueue", 9),
    ("enqueue", 10),
    ("enqueue", 11),
    ("enqueue", 12),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("dequeue", None),
    ("peek", None),
    ("dequeue", None),
    ("peek", None),
    ("enqueue", 13),
    ("enqueue", 14),
    ("enqueue", 15),
    ("enqueue", 16),
    ("dequeue", None),
    ("peek", None),
    ("enqueue", 17),
    ("enqueue", 18),
    ("dequeue", None),
    ("peek", None),
    ("enqueue", 19),
    ("enqueue", 20),
    ("enqueue", 21),
    ("peek", None),
  
]    
#end of chatgpt
    

arrayQueue = CircularQueueArray(10)
linkedListQueue = CircularQueueLinkedList()

for implementation in [arrayQueue, linkedListQueue]:
    for operation, expected_value in operations:
        real_value = None

        if operation == "enqueue":
            implementation.enqueue(expected_value)
        elif operation == "dequeue":
            real_value = implementation.dequeue()
        elif operation == "peek":
            real_value = implementation.peek()

        
        print(f"Operation: {operation}({expected_value}), Expected Value: {expected_value}")

    if implementation == arrayQueue:
        print("Finished with CircularQueueArray, proceeding with CircularQueueLinkedList")


