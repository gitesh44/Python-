import random

computer=random.choice([-1,0,1])
yourstr = input("Enter your choice Snake(s) Water(w) Gun(g): ") #take input as string
youDict = {'s':-1,'w':0,'g':1} #to convert string input to corresponding number
reverseDict = {-1:'Snake',0:'Water',1:'Gun'} #to convert number back to string
you=youDict[yourstr] #convert your string input to corresponding number

#By now we have computer and you values
print(f"You chose {reverseDict[you]} and computer chose {reverseDict[computer]}")

if you == computer:
    print("It's a tie")
elif (you == -1 and computer == 0) or (you == 0 and computer == 1) or (you == 1 and computer == -1): #conditions where you win
    print("You win") 
else:
    print("Computer wins")
# -1 : Snake
# 0 : Water
# 1 : Gun

