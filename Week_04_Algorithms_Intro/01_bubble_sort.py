"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def bubble():
    blist = []
    check = True
    while check == True:
        user = int(input("enter a number "))
        done = input("enter done if finished")
        blist.append(user)
        if done == "done":
            print(blist)
            for i in range(len(blist)):
                for j in range(len(blist)-1):
                    if blist[j] > blist[j + 1]:
                        temp = blist[j]
                        blist[j] = blist[j + 1]
                        blist[j + 1] = temp
            check = False
        else:
            check = True
    return blist

sort = bubble()
print(sort)
