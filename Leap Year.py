def leap(k):
    if l%4==0:
        if l%100==0:
            if l%400==0:
                print('The Year You Entered is a Leap Year')
            else:
               print('The Year You Entered is not a Leap Year')
        else:
            print('The Year You Entered is a Leap Year')
    else:
        print('The Year You Entered is not a Leap Year')

l=int(input('Year: '))
leap(l)
