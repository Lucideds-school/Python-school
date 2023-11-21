import base64
import random
import string
f = open("/workspaces/Python-school/Other/PasswordFileOpen/PasswordFileOpen.txt", "r")

def make_password():
    list = string.ascii_letters
    pass_length = 8
    global random_pass
    random_pass = ''.join(random.choice(list) for i in range(pass_length))

def user_create():
    global username
    global encr
    print("Create a username and password")
    username = input("Enter a username: ")
    print(f"Recommended password: {random_pass}")
    pas = input("Enter a password: ")
    pas_byt = pas.encode("ascii")
    print("Username and password set.")
    encr = base64.b64encode(pas_byt)

def file_open():
    user_login = input("Username: ")
    if user_login == username:
        user_password = input("Password: ")
        decryp = base64.b64decode(encr)
        decrypt = decryp.decode("ascii")
        if user_password == decrypt:
            print("Logged in successfully.")
            contents = print(f.read())
        else:
            print("Password incorrect, please try again.")        
    else:
        print("Username not found, please try again.")

make_password()
user_create()
file_open()