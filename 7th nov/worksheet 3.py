def maths(a, b):
    bru = input("u want add, multiply, minus or divide ")
    if bru == "add":
        ans = a+b
        user = int(input(f"what is {a} + {b} "))
        if user == ans:
            print("good job u got it right")
        else:
            print(f"u wrong it was {ans}")
    if bru == "multiply":
        ans = a*b
        user = int(input(f"what is {a} x {b} "))
        if user == ans:
            print("good job u got it right")
        else:
            print(f"u wrong it was {ans}")
    if bru == "minus":
        ans = a-b
        user = int(input(f"what is {a} - {b} "))
        if user == ans:
            print("good job u got it right")
        else:
            print(f"u wrong it was {ans}")
    if bru == "divide":
        ans = a/b
        user = float(input(f"what is {a} ÷ {b} "))
        if user == ans:
            print("good job u got it right")
        else:
            print(f"u wrong it was {ans}")
a = int(input("wat number u wanna use for num 1 "))
b = int(input("wat abt num 2 "))
maths(a, b)
