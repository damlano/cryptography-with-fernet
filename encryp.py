from cryptography.fernet import Fernet 
import os
# imports

def get_user_input(question): # defining my get_user_input function which ill use later
    while True:
        try:
            user_input = str(input(question))
            if os.path.exists(user_input):
                return user_input
                break
            else:
                print('Please enter a valid file')
        except ValueError:
            print('Please enter a valid file')


keyfile = input("Where do you want the key to be stored? ") 
if keyfile.find(".") == -1: 
    keyfile = keyfile + ".txt" # add .txt if user didnt give any extension

filetoencrypt = get_user_input("What file do you want to encrypt? ")
    
key = Fernet.generate_key() #generate the key

# undere here it writes to the key file sents the key there and changes everything to be unreadable
with open(keyfile, "wb") as fh:
    fh.write(key)

with open(filetoencrypt, "rb") as fh:
    original = fh.read()

f = Fernet(key)
token = f.encrypt(original)

with open(filetoencrypt, "wb") as fh:
    fh.write(token)
