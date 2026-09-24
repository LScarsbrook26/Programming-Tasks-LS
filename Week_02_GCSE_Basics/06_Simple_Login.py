"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def login(username, password):
    for i in range(3):
        user = input("Enter username: ")
        pass1 = input("Enter password: ")
        if user == username and pass1 == password:
            print("Welcome!")
            break
        else:
            print("Access denied:", 2 - i, "attempts remaining")
    else:
        print("Too many failed attempts.")

username = "LScarsbrook"
password = "M1lkshake!"
signin = login(username, password)

