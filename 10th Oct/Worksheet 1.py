import random
number = 1
guesses = 1
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number and guesses <= 2:
  print("Incorrect")
  guesses = guesses + 1
  print("Guess a number between 1 and 10")
  guess = int(input())
if guesses != 3:
    print(f"Correct, you got it in {guesses} attempt(s).")
else:
    print("Incorrect, you failed")
