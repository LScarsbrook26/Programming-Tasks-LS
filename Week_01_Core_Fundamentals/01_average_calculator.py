"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def calculate_average():
   numbers = []
   add = True
   while add == True:
       entry = int(input("Enter a number: "))
       fin = input("enter done if finished, else put anything")
       numbers.append(int(entry))
       if fin == "done":
           add = False
       else:
           add = True
   total = 0
   for i in range(len(numbers)):
       total = total + int(numbers[i])

   average = total / len(numbers)
   return average

calculator = calculate_average()
print("Your average is:", calculator)
