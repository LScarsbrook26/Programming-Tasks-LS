"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def multiplier(num):
   table = []
   for i in range(1,13):
       ans = i * num
       table.append(ans)
   return table

num = int(input("enter number gor its times table, 1-12: "))
cal = multiplier(num)
print(cal)
