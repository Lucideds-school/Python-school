answer = 0 
times_table = int(input("What times table do you want ")) 
bru = int(input("How high do u want "))
bru = bru + 1
print(f"Here is the {times_table} times table") 
for x in range(1, bru): 
    answer = x * times_table 
    print(f"{x} times {times_table} is {answer}")