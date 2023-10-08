print("Pick either Carrot, Broccoli, Peas, or Sweetcorn. I will attempt to guess your choice.")
ans = input("Is the vegetable green? Y/N ")
if ans.lower() == "y":
    ans = input("Does the vegetable look like a tree? Y/N ")
    if ans.lower() == "n":
        print("Your vegetable is peas!")
    else:
        print("Your vegetable is Broccoli!")
elif ans.lower() == "n":
    ans = input("Is your vegetable yellow? Y/N ")
    if ans.lower() == "y":
        print("Your vegetable is sweetcorn!")
    else:
        print("Your vegetable is a carrot!")