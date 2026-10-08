"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def insertion():
    ilist = []
    check = True
    while check == True:
        user = int(input("enter a number "))
        done = input("enter done if finished ")
        ilist.append(user)
        if done == "done":
            print(ilist)
            for i in range(1, len(ilist)):
                current = ilist[i]
                j = i - 1
                while j >= 0 and ilist[j] > current:
                    ilist[j + 1] = ilist[j]
                    j = j - 1
                ilist[j + 1] = current
            check = False
        else:
            check = True

    return ilist


sort = insertion()
print(sort)
