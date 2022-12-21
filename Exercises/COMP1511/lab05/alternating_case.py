def make_cap(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return chr(ord(letter) - ord('a') + ord('A'))
    
    return letter

def make_lower(letter):
    if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
        return chr(ord(letter) - ord('A') + ord('a'))

    return letter

def read_input():
    line = input()

    result = []
    letter_count = 0;  
    for i in range(len(line)):
        if line[i].isalpha():
            if letter_count % 2 != 0:
                result.append(make_cap(line[i]))
            else:
                result.append(make_lower(line[i]))
            letter_count += 1
        else: 
            result.append(line[i])
    
    return ''.join(result)

print(read_input())

