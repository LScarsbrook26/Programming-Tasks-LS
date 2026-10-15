"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    file = open("contacts.txt", "a")
    file.write(name + "," + phone + "," + email + "\n")
    file.close()

def search():
    search_name = input("Enter name to search for: ")
    file = open("contacts.txt", "r")
    found = False
    for line in file:
        contact = line.strip().split(",")
        if contact[0].lower() == search_name.lower():
            print("Name:", contact[0])
            print("Phone:", contact[1])
            print("Email:", contact[2])
            found = True
    file.close()
    if found == False:
        print("Contact not found")


def display():
    file = open("contacts.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

choice = ""
while choice != "4":
    print("menu")
    print("1. add contact")
    print("2. search contact")
    print("3. display all contacts")
    print("4. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        display()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice")
