answer = 0 
times_table = int(input("What times table do you want ")) 
bru = int(input("How high do u want "))
bru = bru + 1
print(f"Here is the {times_table} times table") 
for x in range(bru): 
    answer = x * times_table 
    print(f"{times_table} x {x}")
    pls = int(input("what is the answer??? "))
    if pls == answer:
        print("good job !!1!!1")
    else:
        print("worng >:( ")