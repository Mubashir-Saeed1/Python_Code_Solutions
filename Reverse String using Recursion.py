def reverse(string, reversed_string=None):
    if reversed_string is None:
        reversed_string = ''
    if len(string) < 1:
        return reversed_string
    reversed_string += string[-1]
    return reverse(string[:-1], reversed_string)


print(reverse('Hello World'))
