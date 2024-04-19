
def decrypt(line, mapping):
    inverse = mapping.copy()
    inverse[1] = '!'
    for i in range (26):
        inverse[ord(mapping[i]) - ord('a')] = chr(ord('a') + i)

    result = []
    for i in range(len(line)):
        if line[i] >= 'a' and line[i] <= 'z':
            result.append(inverse[ord(line[i]) - ord('a')])
        elif line[i] >= 'A' and line[i] <= 'Z':
            result.append(chr(ord(inverse[ord(line[i]) - ord('A')]) - ord('a') + ord('A')))
        else: result.append(line[i])
    
    return ''.join(result)

def read_input():
    print("Enter mapping: ")
    mapping = [*input()]
   
    print("Enter text: ")
    while True: 
        try:
            line = input()
            print(decrypt(line, mapping))
        except EOFError:
            break

read_input()