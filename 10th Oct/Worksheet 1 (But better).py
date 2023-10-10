import random
num = random.randint(1, 10)
guesses = 0
print("Guess the number! 1/10")
while True:
    ans = int(input())
    if ans == num:
        print(f"Good job! you guessed it in {guesses}!")
        break
    else:
        print("Incorrect try again.")
        guesses = guesses + 1
