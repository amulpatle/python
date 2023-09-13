import random
cNumber = random.randrange(1,101)
userNumber = int(input("Enter a number :-"))

if cNumber > userNumber:
    print("Computer Number is ",cNumber)
    print("Your Number Is Too Low")
elif cNumber<userNumber:
    print("Computer Number is ",cNumber)
    print("Your Number Is Too High")
else:
    print("Computer Number is ",cNumber)
    print("Your Number Is Equal To Computer Number")