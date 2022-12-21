
def word_square():
    while True:
        try:
            word = input("Input word: ")
            print()
            print("Word square is: ")
            for i in range(len(word)):
                print(word)
        except EOFError:
            break

word_square()