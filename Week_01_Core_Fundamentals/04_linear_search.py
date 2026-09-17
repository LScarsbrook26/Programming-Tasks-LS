"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def linear_search(target):
    value = []
    for i in range(0,10):
        num = random.randint(0,10)
        value.append(num)
    print(value)
    found = 0
    for i in range(len(value)):
        if value[i] == target:
            found = i
    
    return found

target = int(input("enter the number your looking for: "))
add = linear_search(target)
if add == 0:
    print("wasn't found")
else:
    print(target, "was found at index", add)
