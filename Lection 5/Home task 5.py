
text = input("Enter your text: ")

for symbol in text:
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            print(f"This is digit {symbol} and is even")
        else:
            print(f"This is digit {symbol} and is odd")
    elif symbol.isalpha():
        if symbol.isupper():
            print(f"This is letter {symbol} and it is in upper case")
        else:
            print(f"This is letter {symbol} and it is in lower case")
    else:
        print("This is symbol")
