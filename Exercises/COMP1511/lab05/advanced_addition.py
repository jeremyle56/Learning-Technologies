MAX_SIZE = 101

def add_stuff(values, num_rows, num_cols):
    col = num_cols - 1
    carry = 0
    while col >= 0:
        sum = carry
        for row in range(num_rows):
            sum += values[row][col]
            row += 1
        values[num_rows][col] = sum % 10
        carry = int(sum / 10)
        col -= 1
    return carry

def read_input():
    rows = int(input("Enter the number of rows (excluding the last): "))
    cols = int(input("Enter the number of digits on each row: "))

    values = [[0 for i in range(MAX_SIZE)] for i in range(MAX_SIZE - 1)] 
    for i in range(rows):
        line = input()
        line = line.split()
        for j in range(cols):
            values[i][j] = int(line[j])
    
    carry = add_stuff(values, rows, cols)

    for j in range(cols):
        print(str(values[rows][j]) + ' ', end = "")
    print() 

    if carry > 0:
        print("Carried over: " + str(carry) + "\n")

read_input()
