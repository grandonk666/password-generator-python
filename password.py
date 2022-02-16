import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
digit = string.digits


def generate(length, with_symbols):
    character = lower + upper + digit
    if(with_symbols):
        character += symbol
    password = "".join(random.sample(character, length))
    return password
