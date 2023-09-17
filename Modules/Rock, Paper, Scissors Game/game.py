import random

li = ['rock','paper','seciors']
cChoice = random.choice(li)

while(True):

    uc = int(input('''
1 game start
2 Exit
                   
'''))
    ucount = 0
    ccount = 0
    
    if uc == 1:
        for a in range(1,6):
            userInput = int(input('''
1 rock
2 seciors
3 paper
                                
'''))
            if userInput == 1:
                uchoice = 'rock'
            elif userInput ==2:
                uchoice = 'seciors'
            elif userInput == 3:
                uchoice = 'paper'
            
            cChoice = random.choice(li)
            # print(cChoice)
            # print(uchoice)


            if uchoice == cChoice:
                print("Game draw")
                print("user choice is ", uchoice)
                print("computer choice is ", cChoice)
                ucount = ucount+1
                ccount = ccount+1
            elif(uchoice == 'rock' and cChoice == 'scissor') or (uchoice == 'paper' and cChoice == 'rock') or (uchoice == 'scissor' and cChoice == 'paper'):
                ucount = ucount+1
                print("you won")
                print("user choice is ", uchoice)
                print("computer choice is ", cChoice)
            else:
                ccount = ccount+1
                print("coumputer won")
                print("user choice is ", uchoice)
                print("computer choice is ", cChoice)


    else:
        break
    print("user won ",ucount," times")
    print("computer won ",ccount," times")        
    