from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key

m_pwd = input("What is your master password?")
key = load_key() + m_pwd.encode()
fer = Fernet(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
         data = line.rstrip()
         user , passw = data.split("|")
         print("User:" , user , " | Password:" , fer.decrypt(passw.encode()).decode())

def add():
    u_name = input("Enter user name: ")
    u_pwd = input("Enter password: ")

    with open ("password.txt", 'a') as f:
        f.write(u_name + "|" + fer.encrypt(u_pwd.encode()).decode() +  "\n")


while True:
 mode = input("Would you like to add a new password or view the existing ones?(view, add), press q to exit: ").lower()
 if mode == 'q':
    break
 if mode == "view":
   view()
 elif mode == "add":
   add()
 else:
     print("Invalid Passowrd.")
     continue
