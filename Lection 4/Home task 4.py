text = input('Enter your text: ')

if text.isdigit():
    if int(text) % 2 == 0:
        print(f'This is number {text} and it is even')
    else:
        print(f'This is number {text} and it is odd')
else:
    print(f'This is text and it length is {len(text)}')
