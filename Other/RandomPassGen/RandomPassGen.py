import random
import string
f = open("/workspaces/Python-school/Other/RandomPassGen/RandomPassGen.txt" , "r")
pass_count = 0
chars = string.ascii_letters
pass_length = int(input("How long do you want the passwords to be?: "))
pass_count = int(input("How many passwords do you want?: "))
for i in range (pass_count):
    random_pass = ''.join(random.choice(chars) for i in range(pass_length))
    f.write(random_pass)
