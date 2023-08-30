userInput = input('Enter a string: ')
lowercase = ''
uppercase = ''
for char in userInput[::1]:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char
print('Your string with all lower case letters in the front and spaces removed from the entire string is: ', lowercase, uppercase)