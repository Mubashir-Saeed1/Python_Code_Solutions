class Queue:
    def __init__(self):
        self.__item = []

    def enqueue(self, item):
        self.__item.insert(0, item)

    def dequeue(self):
        return self.__item.pop()

    def isEmpty(self):
        if self.__item:
            return False
        else:
            return True

    def size(self):
        return len(self.__item)


queue = Queue()
print(queue.isEmpty())
queue.enqueue('Name')
print(queue.isEmpty())
queue.enqueue('NoName')
print(queue.dequeue())
print(queue.size())