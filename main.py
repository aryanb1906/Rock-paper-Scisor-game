import random
'''
1 for rock
-1 for scisior
0 for  paper
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"r": 1, "s": -1, "p": 0}
reverseDict = {1: "rock", -1: "scisior", 0: "paper"}

you = youDict[youstr]


print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
