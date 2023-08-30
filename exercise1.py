userInput = input('Enter a string: ')
reversedString = ""
for char in userInput[::-1]:
    reversedString += char
print('your string backwards is: ', reversedString)