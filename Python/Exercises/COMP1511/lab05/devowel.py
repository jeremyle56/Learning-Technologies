
def devowel():
    vowels = 'aeiou'

    while True:
        try:
            line = input()
            print(''.join([l for l in line if l not in vowels]))
        except EOFError:
            break

devowel()