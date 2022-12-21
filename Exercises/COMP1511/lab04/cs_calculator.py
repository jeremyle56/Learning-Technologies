
def calculate(line):
    line = line.split()
    if line[0] == 's':
        return int(line[1]) * int(line[1]) 
    elif line[0] == 'p':
        return pow(int(line[1]), int(line[2]))

def read_input():
    while True:
        try:
            line = input("Enter instruction: ")
            print(calculate(line))
        except EOFError:
            break

read_input()