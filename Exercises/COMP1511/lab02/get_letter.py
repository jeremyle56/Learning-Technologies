
uppercase = input("Uppercase: ")
index = int(input("Index: "))

result = 'a'
if uppercase == 'y':
    result = ord('A') + index
elif uppercase == 'n':
    result = ord('a') + index
else:
    result = "Invalid Input"

print("The letter is " + chr(result))