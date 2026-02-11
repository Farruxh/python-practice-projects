import random

target_val = random.randint(1, 100)
while True:
    user_val = input("Guess the number or press Q to Quit : ")
    if (user_val == "Q"):
        break
    user_val = int(user_val)
    if (user_val == target_val):
        print("You have guessed correct number")
        break
    elif (user_val < target_val):
        print("Your number is too small, guess a bigger value")
        
    else:
        print("Your number is too big, guess a smaller value")

print("----Game Over----")