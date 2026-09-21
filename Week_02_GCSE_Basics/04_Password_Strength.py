"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def check(password):
    total = 0
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    
    if len(password) >= 8:
        total = total + 1
    if any(char.isdigit() for char in password):
        total = total + 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        total = total + 1
    if any(char in special_characters for char in password):
        total = total + 1

    if total <= 1:
        return "Weak"
    elif total == 2 or total == 3:
        return "Medium"
    else:
        return "Strong"


password = input("Enter your password: ")
strength = check(password)
print("Password strength:", strength)
