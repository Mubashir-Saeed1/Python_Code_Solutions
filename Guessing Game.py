i=0
print('You have only five Tries')
print('Guess a Number Between 0 & 10:')
while i<=5:
    n=int(input())
    if n>6:
        print('The Number is less than the Number you Entered')
    elif n<6:
        print('The Number is Greater than the Number you Entered')
    else:
        print('___@@@Cogratulations!!!You Won the Game@@@___')
        break
    i+=1
else:
    print('<<<---Sorry, You Lost--->>>')
