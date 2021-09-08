class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def reverse(head):
    current = head
    prev = None
    while current:
        nextNode = current.nextNode
        current.nextNode = prev
        prev = current
        current = nextNode
    return prev



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextNode = b
b.nextNode = c
c.nextNode = d
reverse(a)
print(d.value)
print(d.nextNode.value)
print(c.nextNode.value)
print(b.nextNode.value)
print(a.nextNode.value)
