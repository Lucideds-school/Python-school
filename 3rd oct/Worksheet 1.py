cost = 0
crust = input("Thin or thick crust? ")
size = int(input("What size in inches? 8, 10, 12, 14 or 18? "))
cheese = input("Do you want cheese? y/n ")
type = input("Which pizza type would you like? Margherita, Vegetable, Vegan, Hawaiian or Meat Feast? ")
voucher = input("If you have a voucher code, enter it now, Press enter to skip. ")
if crust.lower() == "thin":
    cost = cost + 10
else: 
    cost = cost + 8
if size > 10:
    cost = cost + 2
if cheese.lower() == "n":
    cost = cost - 0.5
if type.lower() == "vegetable" or type.lower() == "vegan":
    cost = cost + 1
elif type.lower() == "hawaiian" or type.lower() == "meat feast":
    cost = cost + 2
if size == 18 and voucher.lower() == "funfriday":
    cost = cost - 2
print(f"Your pizza costs, £{cost}")


