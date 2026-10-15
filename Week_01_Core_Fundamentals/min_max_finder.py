"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
def find_min_max():
    numbers = []
    add = True
    while add == True:
        num = int(input(" enter number: "))
        numbers.append(num)
        fin = input("enter done if finished, else anything")
        if fin == "done":
            add = False
        else:
            add = True
    maxNum = numbers[0]
    minNum = numbers[0]
    for num in numbers:
        if num > maxNum:
            maxNum = num
        else:
            maxNum = maxNum
        
        if num < minNum:
            minNum = num
    
    total = [maxNum,minNum]
    return total

values = find_min_max()
print("your max and min values are: ", values)
