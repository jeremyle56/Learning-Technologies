
def count_up_down():
    num = int(input("Enter number: "))

    i = 0
    if num > 0:
        while i <= num:
            print(i)
            i += 1
    elif num < 0:
        while i >= num:
            print(i)
            i -= 1

count_up_down()