def balanced_parentheses(string):
    l_string = list(string)
    flag = False
    opened = []
    closed = ''
    for x in range(len(l_string)):
        if l_string[x] == '(' or l_string[x] == '{' or l_string[x] == '[':
            opened.append(l_string[x])
        else:
            if l_string[x] == ']':
                closed = '['
            elif l_string[x] == '}':
                closed = '{'
            elif l_string[x] == ')':
                closed = '('
            if closed == opened[-1]:
                flag = True
                opened.remove(opened[-1])
            else:
                flag = False
    return flag


t = balanced_parentheses('[]')
print(t)
t1 = balanced_parentheses('[](){([[[]]])}')
print(t1)
t2 = balanced_parentheses('()()[}')
print(t2)
t3 = balanced_parentheses('[[{}]]')
print(t3)
