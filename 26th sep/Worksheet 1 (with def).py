import time
print("Welcome to the 'JOKE MACHINE'")
count = 0
def joke(que, ans, ans2):
    print("Guess the punchline...")
    time.sleep(0.8)
    x = input(que).lower()
    if x == ans.lower() or x == ans2.lower():
        print("Correct!")
        count = count =+ 1
    else:
        print("Wrong. It is","'"+ans+"'")

joke("What is pink and fluffy? ", "Pink fluff", "Pink fluff")
joke("What is brown and sticky? ", "A brown stick", "brown stick")
joke("What is black and white and red all over? ", "A newspaper", "newspaper")