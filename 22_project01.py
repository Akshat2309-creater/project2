'''
python project on snake , water and gun 
1 : snake
-1 : water
0 : gun
'''
# import random module for random choice
import random
computer = random.choice([1,-1,0])
youstr = input("enter your choice:")
# creating dictonary with key-values
youdict = {"s":1 ,"w" : -1, "g" : 0}
reversedict = {1 : "Snake" , -1 : "water" , 0 : "gun"}

you = youdict[youstr]
print(f"your choice :{reversedict[you]}\n computer choice :{reversedict[computer]}")

# using conditional statements

if(computer == you):
    print("it is a draw!")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!!")
    elif(computer == 0 and you == -1):
        print("you win!!")
    elif(computer == 0 and you == 1):
        print("you lose!!")


print("something went wrong")

    
    
    
