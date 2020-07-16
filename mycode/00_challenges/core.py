# Importing from your own code

# Create two files, named "core.py" and "app.py"

# Inside of your core.py file, create a function named silly_strings
# The silly_strings function should take one parameter, a list of strings

# example words

def silly_strings(words):
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    txt = ""
    for word in words:
        if word.startswith(VOWELS):
            txt += f"{word}ay "
        else:
            txt += f"{word[1:]}{word[:1]}ay "
    return txt
words = ["sam", "bill", "Me"]
print(silly_strings(words))
