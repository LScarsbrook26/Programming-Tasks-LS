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
