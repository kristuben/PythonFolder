def FizzBuzzz(number1,number2):
    return number1%number2==0

'''b=3
c=5
d=15
#calling function
multiple3= MultipleofThree(a,b)
multiple5= MultipleofFive(a,c)
multiple15= MultipleofThreeFIve(a,d)'''

a="hfth"
while(True):
    a=input("choose a number ")
    if a=="stop":
        break
    a=int(a)
    if FizzBuzzz(a,15):
        print("FizzBuzz")
    elif FizzBuzzz(a,3):
        print("Fizz")
    elif FizzBuzzz(a,5):
        print("Buzz")
    else:
        print('try again')
