import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
digit = string.digits

character = lower + upper + symbol + digit


def generate(length):
    password = "".join(random.sample(character, length))
    return password
