"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

array = [
    [2, 6, 5],
    [4, 9, 8]
]


def add():
    row = int(input("Which row? "))
    value = int(input("Enter value: "))
    array[row].append(value)


def read():
    for i in array:
        print(i)


def delete():
    row = int(input("Which row? "))
    position = int(input("Which position? "))
    array[row].pop(position)


print("1 - add")
print("2 - read")
print("3 - delete")
choice = input("choose: ")
if choice == "1":
    add()
elif choice == "2":
    read()
else:
    delete()
