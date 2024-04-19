
def scanning_into_array():
    how_many_nums = input("How many numbers: ")

    if int(how_many_nums) > 0:
        num = int(input("Please enter numbers: "))
        nums = [num]
        for i in range(int(how_many_nums) - 1):
            num = int(input())
            nums.append(num)
    
        print("Minimum: " + str(min(nums)))
        print("Maximum: " + str(max(nums)))

scanning_into_array()