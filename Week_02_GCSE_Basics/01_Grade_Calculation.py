"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_grade(score):
    total = "A"
    if score >= 80 and score <= 100:
        total = "A"
    elif score >= 60 and score <= 79:
        total = "B"
    elif score >= 40 and score <= 59:
        total = "c"
    else:
        total = "D"
    return total

score = int(input("enter percentage: "))
cal = get_grade(score)
print(cal)

