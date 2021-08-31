import queue
# fifo = queue.Queue(size)

fifo = queue.Queue()
lifo = queue.LifoQueue() # Last in First Out
simple = queue.SimpleQueue() # Fifo
priority = queue.PriorityQueue() # respect priority of messages

# Adding a message in queue - put method
message = "Message {} ".format(1)
fifo.put(message)
lifo.put(message)
simple.put(message)
priority.put(message)

# Checking Size
print(fifo.qsize())
print(lifo.qsize())
print(simple.qsize())
print(priority.qsize())

for i in range(2,10):
    lifo.put("Message {} ".format(i))
    simple.put("Message {} ".format(i))

print(lifo.qsize())
print(simple.qsize())

# getting message from queue
print("fifo.get() " , fifo.get())
print("lifo.get() " , lifo.get())
print("simple.get() " , simple.get())
print("priority.get() " , priority.get())

print(fifo.qsize())
print(lifo.qsize())
print(simple.qsize())
print(priority.qsize())
