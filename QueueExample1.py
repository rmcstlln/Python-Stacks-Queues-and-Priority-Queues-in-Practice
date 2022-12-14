from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

fifo.dequeue()
print(fifo)
fifo.dequeue()
print(fifo)
fifo.dequeue()
print(fifo)
