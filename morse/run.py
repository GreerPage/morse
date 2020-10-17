from .translate import char_to_morse
from .lights import letterspace

def text_to_morse(text):
    t = text.lower().split()
    for word in t:
        for char in word:
            char_to_morse(char)
        letterspace()
    print()
        
