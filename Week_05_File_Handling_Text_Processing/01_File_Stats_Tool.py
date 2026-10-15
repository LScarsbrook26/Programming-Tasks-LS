"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def lines(text):
    lines = text.split("\n")
    return len(lines)

def countwords(text):
    words = text.split()
    return len(words)

def countcharacters(text):
    return len(text)

def freword(text):
    words = text.split()
   



file = open("text.txt", "r")
text = file.read()
file.close()
print("Number of lines:", lines(text))
print("Number of words:", countwords(text))
print("Number of characters:", countcharacters(text))
print("Most frequent word:", freword(text))

