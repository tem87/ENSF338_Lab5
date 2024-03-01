#Part 1:
from array import array

class ArrayQueue:
    def __init__(self):
        # 'i' represents the type code for signed integers
        self.items = array('i')

    def enqueue(self, item):
       
        self.items.insert(0, item)
        print("Enqueue {} | Queue: {}".format(item, list(self.items)))

    def dequeue(self):
        if not self.is_empty():
      
            item = self.items.pop()
            print("Dequeue {} | Queue: {}".format(item, list(self.items)))
            return item
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

#Part 2:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head

    def dequeue(self):
        if not self.is_empty():
            item = self.tail.data

            if self.head == self.tail:
                # If there is only one element in the queue
                self.head = self.tail = None
            else:
                # Traverse the list to find the second-to-last node
                current = self.head
                while current.next.next is not None:
                    current = current.next

                current.next = None
                self.tail = current

            return item
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

#Part3
import random

def generate_random_tasks():
    task_list = []
    probabilities = [0.7, 0.3]  # Probabilities for enqueue and dequeue

    for _ in range(10000):
        task_type = random.choices(["enqueue", "dequeue"], weights=probabilities)[0]

        if task_type == "enqueue":
            task_list.append(("enqueue", random.randint(1, 70)))  # You can replace this with your specific enqueue task
        elif task_type == "dequeue":
            task_list.append(("dequeue", random.randint(1, 30)))

    return task_list
#Part4
import timeit
import random

def test_array_queue():
    array_queue = ArrayQueue()
    for _ in range(1000):
        item = random.randint(1, 100)
        array_queue.enqueue(item)
        array_queue.dequeue()

def test_linked_list_queue():
    linked_list_queue = LinkedListQueue()
    for _ in range(1000):
        item = random.randint(1, 100)
        linked_list_queue.enqueue(item)
        linked_list_queue.dequeue()

# Measure the performance for enqueue operation using timeit
array_enqueue_time = timeit.timeit(test_array_queue, number=100)

linked_list_enqueue_time = timeit.timeit(test_linked_list_queue, number=100)

# Print the results for enqueue operation
print("Array Enqueue Time:", array_enqueue_time)
print("Linked List Enqueue Time:", linked_list_enqueue_time)

# Now, measure the performance for dequeue operation using timeit
def test_array_dequeue():
    array_queue = ArrayQueue()
    for _ in range(1000):
        item = random.randint(1, 100)
        array_queue.enqueue(item)
        array_queue.dequeue()

def test_linked_list_dequeue():
    linked_list_queue = LinkedListQueue()
    for _ in range(1000):
        item = random.randint(1, 100)
        linked_list_queue.enqueue(item)
        linked_list_queue.dequeue()

array_dequeue_time = timeit.timeit(test_array_dequeue, number=100)
linked_list_dequeue_time = timeit.timeit(test_linked_list_dequeue, number=100)

# Print the results for dequeue operation
print("Array Dequeue Time:", array_dequeue_time)
print("Linked List Dequeue Time:", linked_list_dequeue_time)

#Part5
import timeit
import matplotlib.pyplot as plt
import random

# Your ArrayQueue and LinkedListQueue implementations go here

def measure_performance():
    array_enqueue_times = []
    linked_list_enqueue_times = []
    array_dequeue_times = []
    linked_list_dequeue_times = []

    for _ in range(100):
        # Create instances of queues
        array_queue = ArrayQueue()
        linked_list_queue = LinkedListQueue()

        # Enqueue operation
        array_enqueue_time = timeit.timeit(lambda: array_queue.enqueue(random.randint(1, 100)), number=1000)
        linked_list_enqueue_time = timeit.timeit(lambda: linked_list_queue.enqueue(random.randint(1, 100)), number=1000)

        array_enqueue_times.append(array_enqueue_time)
        linked_list_enqueue_times.append(linked_list_enqueue_time)

        # Dequeue operation
        array_dequeue_time = timeit.timeit(lambda: array_queue.dequeue(), number=1000)
        linked_list_dequeue_time = timeit.timeit(lambda: linked_list_queue.dequeue(), number=1000)

        array_dequeue_times.append(array_dequeue_time)
        linked_list_dequeue_times.append(linked_list_dequeue_time)

    return (
        array_enqueue_times,
        linked_list_enqueue_times,
        array_dequeue_times,
        linked_list_dequeue_times
    )

def plot_distribution(array_enqueue_times, linked_list_enqueue_times, array_dequeue_times, linked_list_dequeue_times):
    # Plotting
    plt.figure(figsize=(12, 6))

    # Enqueue operation
    plt.subplot(1, 2, 1)
    plt.hist([array_enqueue_times, linked_list_enqueue_times], bins=20, alpha=0.5, label=['Array Enqueue', 'Linked List Enqueue'])
    plt.title('Distribution of Enqueue Times')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend()

    # Dequeue operation
    plt.subplot(1, 2, 2)
    plt.hist([array_dequeue_times, linked_list_dequeue_times], bins=20, alpha=0.5, label=['Array Dequeue', 'Linked List Dequeue'])
    plt.title('Distribution of Dequeue Times')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Measure performance
array_enqueue_times, linked_list_enqueue_times, array_dequeue_times, linked_list_dequeue_times = measure_performance()

# Plot distribution
plot_distribution(array_enqueue_times, linked_list_enqueue_times, array_dequeue_times, linked_list_dequeue_times)


# Results
'''
According to the graph generated by the code it can be seen that linked list has a very high frequency with in a very short amount of time where as for
array enqeue we see mutiple smaller or average size frequencies at different times this shows that linked list works faster with enequeing operation than array enqeueing.
It is same for deqeueing operation we see that linked list works faster than arrays with deqeueing operation. (Takes very less time than arrays)
'''
