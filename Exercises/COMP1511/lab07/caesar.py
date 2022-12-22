
def caesar(shift, line):
    result = []
    for i in range(len(line)):
        if line[i] >= 'a' and line[i] <= 'z':
            result.append(chr(ord('a') + (ord(line[i]) - ord('a') + shift) % 26))
        elif line[i] >= 'A' and line[i] <= 'Z':
            result.append(chr(ord('A') + (ord(line[i]) - ord('A') + shift) % 26))
        else: result.append(line[i])
    
    return ''.join(result)

def read_input():
    shift = int(input())

    while True:
        try: 
            line = input()
            print(caesar(shift, line))
        except EOFError:
            break

read_input()