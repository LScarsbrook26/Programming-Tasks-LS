"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def reverse_list():
    add = []
    rev = []
    for i in range(0,10):
        num = random.randint(0,10)
        add.append(num)
    print(add)
    for i in range(9,-1,-1):
        rev.append(add[i])
    
    return rev

add = reverse_list()
print(add)
