#CREATED BY BHISHAN SHARMA
import random

number_to_guess = random.randint(0,100)
if number_to_guess >= 50:
    print("HINT : NUMBER IS BIG")
if number_to_guess <= 50:
    print("HINT : NUMBER IS SMALL")

for i in range(10):
    number_input = int(input("Enter Number : "))
    if number_input < number_to_guess and number_input != 0:
        print("Your number is small!!!")
    if number_input > number_to_guess:
        print("Your number is Large")
    if number_input == number_to_guess:
        print("Hey you won!!!")
        print("number was : ",number_to_guess)
        print("----------")
        exit()
    if number_input == 0:
        exit()
    if i == 5:
        print("You Lose try again!!!")
        exit()