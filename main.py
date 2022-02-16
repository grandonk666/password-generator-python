from password import generate

character_length = int(input("Enter length of character : "))
symbols_input = input("Create password with symbols (y/N) : ").lower()


def include_symbol(input):
    if(input == "y"):
        return True
    if(input == "n"):
        return False


with_symbols = include_symbol(symbols_input)

print(generate(character_length, with_symbols))
