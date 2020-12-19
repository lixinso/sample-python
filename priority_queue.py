
'''

The Python priority queue is built on the heapq module, which is basically a binary heap.



'''


from queue import PriorityQueue

q = PriorityQueue()

input = ['a','c','b']

print("Input:", input)

for x in input:
    q.put(x)


print("From Priority Queue:")
while not q.empty():
    print(q.get())

# https://www.geeksforgeeks.org/priority-queue-in-python/
# https://docs.python.org/3/library/queue.html
