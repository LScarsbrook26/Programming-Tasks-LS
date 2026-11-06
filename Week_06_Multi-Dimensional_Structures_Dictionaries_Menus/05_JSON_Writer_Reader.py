"""
TASK: 05 Json Writer Reader

# Do some research into JSON
Prompt user for:
- Name
- Price
- Quantity
Store items into a JSON file with proper formatting
Then allow the user to open and convert to list of dictionaries and output the summary with averages.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def add():
    name = input("enter name")
    price = float(input("enter price"))
    amount = int("how many "))

    add = {
        "name" : name,
        "price" : price,
        "amount" : amount
    }

add()

with open(, "a") as file:
    current_data = json.load(file)
total = add["price"] + add["amount"]
print(total)
