class Dequeue:
    def __init__(self):
        self.__item = []

    def addRear(self, item):
        self.__item.insert(0, item)

    def removeRear(self):
        return self.__item.remove(self.__item[0])

    def addFront(self, num):
        self.__item.append(num)

    def removeFront(self):
        return self.__item.pop()

    def isEmpty(self):
        if self.__item:
            return False
        else:
            return True

    def size(self):
        return len(self.__item)


dequeue = Dequeue()
