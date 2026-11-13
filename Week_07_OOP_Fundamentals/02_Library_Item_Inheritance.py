"""
TASK: 02 Library Item Inheritance

# This will require you understand how inheritance works
Base class: Item
Attributes: title, year
Subclasses:
- Book - add author attribute
- DVD - add director
Demonstrate polymorphism by iterating a list of mixed objects

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def display(self):
        print("Title:", self.title)
        print("Year:", self.year)


class Book(Item):
    def __init__(self, title, year, author):
        Item.__init__(self, title, year)
        self.author = author

    def display(self):
        print("Book:", self.title)
        print("Year:", self.year)
        print("Author:", self.author)


class DVD(Item):
    def __init__(self, title, year, director):
        Item.__init__(self, title, year)
        self.director = director

    def display(self):
        print("DVD:", self.title)
        print("Year:", self.year)
        print("Director:", self.director)


item1 = Book("Harry Potter", 1997, "J.K. Rowling")
item2 = DVD("frozen", 2013, "chris buck ")
item = [item1, item2]

for i in item:
    item.display()
    print()
