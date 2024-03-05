#QUESTION 5 DISCUSSION
"""
When plotting the performance  of the array and linked list using push and pop, we can see that the array stack has a better 
performance than the linked list stack. This is due to the fact that the array has a constant time complexity of O(1) 
for push and pop operations and on the other hand  the linked list stack has a time complexity of O(n) for push 
and pop operations. The linked list stack has to traverse the entire list to perform the push and pop operations. 
"""

import matplotlib.pyplot as plt
import numpy as np
import timeit
import random as rd

#code from lectures
class stackArray:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def isEmpty(self):
        return len(self._storage) == 0

class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

class stackLinkedList:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval
    def isEmpty(self):
        return self._head is None
   
    
#generate random nlists of 10000 tasks probability 0.7 or 0.3
# used chatgpt
def generateRandomLists(size):
    lists = []
    for i in range(size):
        if rd.random() < 0.7:
            lists.append("push")
        else:
            lists.append("push")
    return lists
#end of chatgpt

def taskExecution(case, taskList):
    for task in taskList:
        if task == "push":
            case.push(rd.randint(1, 100))
        elif task == "pop":
            try:
                case.pop()
            except IndexError:
                pass

taskLists = [generateRandomLists(10000) for _ in range(100)]

def performance(stackType, taskList):
    stack = stackType()
    time_taken = timeit.timeit(lambda: taskExecution(stack, taskList), number=1)
    return time_taken

def plotGraph(arrayTime, linkedListTime):
    plt.hist(arrayTime, alpha=0.5, label='Array Stack')
    plt.hist(linkedListTime, alpha=0.5, label='Linked List Stack')
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Performance Distribution of Array vs. Linked List Stack')
    plt.show()

arrayTime = []
linkedListTime = []

for tasks in taskLists:
    arrayTime.append(performance(stackArray, tasks))
    linkedListTime.append(performance(stackLinkedList, tasks))

plotGraph(arrayTime, linkedListTime)





