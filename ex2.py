#Lab 5 Exercise 2 - (COMPLETED)

'''
Question 5
The second implementation that maintains a sorted array should 
generally be faster for enqueue operations. This is because when a
new element is enqueued, it only needs to find the correct position
to insert the element in the sorted array. The insertion operation
is relatively fast compared to the 1st implementation, which requires
us to sort the entire array every time an element is enqueued. 

'''

import random
import timeit

#Implementation 1 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][0] < right[right_idx][0]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue = merge_sort(self.queue)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0


#Implementation 2
class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        index = 0
        while index < len(self.queue) and self.queue[index][0] < priority:
            index += 1
        self.queue.insert(index, (priority, item))

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0



# Function to generate a random list of tasks
def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 1000)))  # Random priority for enqueue
        else:
            tasks.append(("dequeue", None))
    return tasks

# Function to measure the performance of a priority queue implementation
def measure_performance(priority_queue_class):
    total_time = 0
    for _ in range(100):
        tasks = generate_random_tasks()
        pq = priority_queue_class()
        start_time = timeit.default_timer()
        for task in tasks:
            if task[0] == "enqueue":
                pq.enqueue(task[1], random.randint(1, 1000))  # Random priority for enqueue
            else:
                pq.dequeue()
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / 100

# Measure the performance of both implementations
sorted_pq_time = measure_performance(PriorityQueueSorted)
merge_sort_pq_time = measure_performance(PriorityQueue)

print("Sorted Priority Queue Average Time:", sorted_pq_time)
print("Merge Sort Priority Queue Average Time:", merge_sort_pq_time)

