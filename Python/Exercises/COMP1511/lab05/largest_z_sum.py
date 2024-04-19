MAX_SIZE = 100

def main():
    array = [[0 for i in range(MAX_SIZE)] for i in range(MAX_SIZE)]

    length = int(input("Enter 2D array side length: "))
    print("Enter 2D array values: ")
    for i in range(length):
        line = input()
        line = line.split()
        for j in range(length):
            array[i][j] = int(line[j]) 

    print("The largest z sum is " + str(largest_z_sum(array, length)) + '.')

def largest_z_sum(array, size):
    max_sum = array[0][0] + array[0][1] + array[0][2]\
                          + array[1][1]\
            + array[2][0] + array[2][1] + array[2][2]

    for curr_size in range(3, size + 1):
        for y in range(size - curr_size + 1):
            for x in range(size - curr_size + 1):
                top_row_sum = 0
                for i in range(curr_size - 1):
                    top_row_sum += array[y][x + i]
                
                diagonal_sum = 0
                for i in range(curr_size):
                    diagonal_sum += array[y + i][x + (curr_size - 1) - i]
                
                bottom_row_sum = 0
                for i in  range(curr_size - 1):
                    bottom_row_sum += array[y + (curr_size - 1)][x + i + 1]
                
                total_sum = top_row_sum + diagonal_sum + bottom_row_sum
                if total_sum > max_sum:
                    max_sum = total_sum
            
    return max_sum

main()