choice6=input("You are in McDonalds, do you buy a regular cone or a dipped cone?")
if choice6=='regular cone':
    print("A creepy guy steals your cone.")
    choice1=input('Do you chase after him, throw a shoe at him or buy a new one?')
    if choice1=="chase after him":
        print("You follow him into a desserted home.")
        choice2=input('Do you go in or not, yes or no?')
        if choice2=="yes":
            print("you find him and you get your ice cream cone back. you win!")
        if choice2=="no":
            print('you dont get your ice cream cone back. you lose.')
    if choice1=="buy a new one":
        print("Congratulations, you win. you had to pay more but you got an ice cream cone")
    if choice1=="throw a shoe at him":
        choice3=input('Do you throw left or right')
        if choice3=="left":
            print("you miss and you lose")
        if choice3=="right":
            print('you got your ice cream cone back. but it fell on the ground so you lose.')
    if choice1=="steal a cone from someone else":
        choice4=input('Do you steal from the person to your left or right')
        if choice4=="left":
            print('you win! but you stole from a person so you are just as bad as the person who stole from you')
        if choice5=="right":
            print('you win! but you stole from a person so you are just as bad as the person who stole from you')
if choice6=="dipped cone":
    print("A creepy guy steals your cone.")
    choice1=input('Do you chase after him, throw a shoe at him or buy a new one?')
    if choice1=="chase after him":
        print("You follow him into a desserted home.")
        choice2=input('Do you go in or not, yes or no?')
        if choice2=="yes":
            print("you find him and you get your ice cream cone back. you win!")
        if choice2=="no":
            print('you dont get your ice cream cone back. you lose.')
    if choice1=="buy a new one":
        print("Congratulations, you win. you had to pay more but you got an ice cream cone")
    if choice1=="throw a shoe at him":
        choice3=input('Do you throw left or right')
        if choice3=="left":
            print("you miss and you lose")
        if choice3=="right":
            print('you got your ice cream cone back. but it fell on the ground so you lose.')
    if choice1=="steal a cone from someone else":
        choice4=input('Do you steal from the person to your left or right')
        if choice4=="left":
            print('you win! but you stole from a person so you are just as bad as the person who stole from you')
        if choice5=="right":
            print('you win! but you stole from a person so you are just as bad as the person who stole from you')
