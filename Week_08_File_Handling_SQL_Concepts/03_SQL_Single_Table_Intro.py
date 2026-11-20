"""
TASK: 03 Sql Single Table Intro

# You will need to visit https://www.w3schools.com/python/ref_module_sqlite3.asp
Provide an SQLite database with one table- Tasks:
- Connect using Python sqlite3 import
- Run simple SELECT queries
- Insert new records
- Display table in formatted text output

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        
    
    def peek(self):
        

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

bus = Queue()
bus.enqueue("261")
bus.enqueue("320")
bus.enqueue("61")

print("Buses waiting:", bus.queue)
bus_stop.dequeue()
print("Number of buses:", bus.size())
print("empty?", bus.is_empty())

