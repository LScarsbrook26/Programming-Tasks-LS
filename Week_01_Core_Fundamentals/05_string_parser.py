"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def word_split(sentence):
    add = []
    word = ""
    for i in sentence:
        if i == " ":
            if word != "":
                add.append(word)
                word = ""
        else:
            word = word + i

    if word != "":
        add.append(word)

    return add

sentence = input("Enter a sentence: ")
sep = word_split(sentence)
print("number of words:", len(sep))
print("list of words:", sep)
