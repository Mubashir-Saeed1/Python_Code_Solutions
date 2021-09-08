num1=int(input('Enter Number 1: '))
num2=int(input('Enter Number 2: '))
class switch:
    def add():
        print('Sum = ',num1+num2)
    def sub():
        print('Difference = ',num1-num2)
    def mult():
        print('Product = ',num1*num2)
    def div():
        print('Division = ',num1/num2)
    dic={
        1:add,
        2:sub,
        3:mult,
        4:div
        }
    op=int(input('Enter Operation: '))
    x=dic.get(op)()
