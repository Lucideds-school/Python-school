import time
count = 0
print("Welcome to the 'JOKE MACHINE'")
print("Guess the punchline...")
time.sleep(0.8)
x = input("What is pink and fluffy? ").lower()
if x == "pink fluff":
    print("Correct!")
    count = count =+ 1
else:
    print("Wrong. It is 'Pink Fluff'")
time.sleep(0.8)
print("Try and guess this one...")
time.sleep(0.8)
x = input("What is brown and sticky? ").lower()
if x == "a brown stick" or x == "brown stick":
    print("Correct!")
    count = count =+ 1
else:
    print("Wrong. It is 'A Brown Stick'")
time.sleep(0.8)
print("This is the hardest one...")
x = input("What is black and white and red all over? ").lower()
if x == "a newspaper" or x == "newspaper":
    print("Correct!")
    count = count =+ 1
else:
    print("Wrong. It is 'A Newspaper'")
print("Good job! You got...")
time.sleep(1)
print(count, "Correct!")
