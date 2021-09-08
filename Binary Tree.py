def binary_tree(r):
    return [r, [], []]


def insert_left(root, value):
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1, [value, t, [], []])
    else:
        root.insert(1, [value, [], []])


def insert_right(root, value):
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [value, t, [], []])
    else:
        root.insert(2, [value, t, [], []])


def get_left(root):
    print(root[1])


def get_right(root):
    print(root[2])


def get_root(root):
    print(root[0])


def set_root(root, value):
    root.insert(0, value)


b = binary_tree(3)
print(b)
insert_left(b, 5)
insert_right(b, 4)
get_right(b)
get_left(b)
get_root(b)
set_root(b, 9)
get_root(b)