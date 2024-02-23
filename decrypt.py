from cryptography.fernet import Fernet 
import os

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


keyfile = get_user_input("Where is the key stored? ")
if keyfile.find(".") == -1:
    keyfile = keyfile + ".txt" #adding .txt if no extension is given

filetoencrypt = get_user_input("What file do you want to dencrypt? ")

fh = open(keyfile, "rb")  
key = fh.read() 
fh.close()

fh = open(filetoencrypt, "r")
token = fh.read()
fh.close()

f = Fernet(key)  
abc = f.decrypt(token)

fh = open(filetoencrypt, "wb")
fh.write(abc)
fh.close()

os.remove(keyfile) #auto delete the key 
