"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

file = open("info.txt", "w")
name = input("enter your name ")
age = str(input("enter your age "))
col = input("enter fav colour")
file.write("\n" + name)
file.write("\n" + age)
file.write("\n" + col)
file.close()
add = input("do u want to added anytihng?")
if add == "yes":
    file = open("info.txt", "a")
    add2 = input("write what u want to add: ")
    file.write("\n" + add2)
    file.close()
