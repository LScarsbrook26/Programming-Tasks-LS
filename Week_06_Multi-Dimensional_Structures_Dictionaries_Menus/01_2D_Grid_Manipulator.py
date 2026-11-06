"""
TASK: 01 2D Grid Manipulator

# Create an NxM grid resolver - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
- Initialises a grid filled with zeros
- Allows user to "paint" coordinates
- Displays updated grid each time

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
grid = []
check = True

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    grid.append(row)

print("grid:")
for row in grid:
    print(row)

while check == True:
    print("Enter a coordinate to paint.")
    print("Enter -1 to stop.")
    x = int(input("Enter row number: "))
    y = int(input("Enter column number: "))
    if x >= 1 and x <= rows and y >= 1 and y <= columns:
        grid[x - 1][y - 1] = 1
        print("updated grid:")
        for row in grid:
            print(row)
    elif x == -1 or y == -1:
        for row in grid:
            print(row)
        check = False
    else:
        print("Invalid")
