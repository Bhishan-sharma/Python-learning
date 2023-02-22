import random

rock = 'r'
paper = 'p'
scissor = 's'
quit = 'q'
while(True):
    print("enter 'r' for rock , 's' for scissor , 'p' for paper")
    print("play or quit by 'q'")
    moves = ['r', 'p', 's']
    computer = random.choice(moves)
    player = input("Player: ")
    if(player == computer):
        print("tie " +"computer was "+computer)
        print("###############################################################\n")
    elif(player == quit):
        exit()
    elif(player == rock and computer == paper):
        print("You Lost!" + " computer was " + computer)
        print("################################################################\n")
    elif(player == paper and computer == scissor):
        print("You Lost!" + " computer was " + computer)
        print("################################################################\n")
    elif(player == scissor and computer == rock):
        print("You Lost!" + " computer was " + computer)
        print("################################################################\n")
    else:
        print("you won!" + " computer was " + computer)
        print("#################################################################\n")
