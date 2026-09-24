"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def shopping_list():
    shopping = []
    done = True
    while done == True:
        add = input("add items to shopping list: (enter done if finished adding)")
        shopping.append(add)
        if add == "done":
            print(shopping)
            done = False
        else:
            done = True
    edit = input("do u want to edit the list: yes or no ")
    if edit == "yes":
        num = int(input("enter which number item u want to change: "))
        change = input("enter what u want to change it to ")
        shopping[num - 1] = change
    else: 
        print('finished')
    
    return shopping

paper = shopping_list()
print("completed shopping list:", paper)
