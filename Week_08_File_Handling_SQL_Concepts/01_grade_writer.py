"""
TASK: 01 Grade Writer 

# Purpose is to write a grade uploading program for csv files
Ask the user for student names and ages, with a keyword to stop.
Writes all entries to a .txt file and .csv file separately

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def grade():
    students = []
    name = input("enter student name, ( stop to finish )")
    while name != "stop":
        age = input("enter student age: ")
        students.append(name, age)
        name = input("enter student name, ( stop to finish )")
    
    return students

def txt(students):
    file = open("grades.txt", "w")
    for i in students:
        file.write(student[0] + " " + student[1] + "\n")
    file.close()

def csv(students):
    file = open("grades.csv", "w")
    file.write("Name,Age\n")
    for i in students:
        file.write(student[0] + "," + student[1] + "\n")
    file.close()


students = grade()
txt(students)
csv(students)
print(txt)
print(csv)
