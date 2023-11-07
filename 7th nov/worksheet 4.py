# dog walking code
def dog(d, w):
    total = d * w
    print(f"Number of dogs: {d}")
    print(f"Number of days walked: {w}")
    print(f"Total number of walks: {total}")
    total = total * 4.00
    print(f"Total cost: {total}")
dogs = int(input("Number of dogs for this client: "))
walks = int(input("How many days has the dog been walked? "))
dog(dogs, walks)
