
def print_grid():
    size = int(input("Enter size: "))

    for i in range(size):
        for j in range(size):
            print("(" + str(i) + ", " + str(j) + ") ", end = "")
            if j == size - 1:
                print()
    print()

print_grid()