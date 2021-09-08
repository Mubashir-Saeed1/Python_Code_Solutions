class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def nth_to_last(n, head):
    count = 0
    empty_head = head
    while empty_head:
        count += 1
        empty_head = empty_head.nextNode
    loop = count - n
    if loop < 0:
        print(f'Please Enter a Number from 0-{count}')
        return
    for x in range(loop):
        head = head.nextNode
    return head.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
print(nth_to_last(8, a))
