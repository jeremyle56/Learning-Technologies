GAP = 4

def xtreme():
    n = int(input("Enter size: "))
    half = n / 2

    for row in range(n): 
        for col in range(n):
            if (row <= half) == (col < half):
                if row % 4 == col % 4:
                    print("*", end = "")
                else:
                    print("-", end = "")
            else:
                if row % GAP == (n - 1 - col) % GAP:
                    print("*", end = "")
                else: 
                    print("-", end = "")
        print()


xtreme()