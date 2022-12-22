
def array_sum_prod(length, nums):
    sum = 0
    prod = 1;
    for i in range(length):
        sum += nums[i]
        prod *= nums[i]
    return sum, prod

def main():
    nums = [3, 4, 1, 5, 6, 1]

    sum, prod = array_sum_prod(6, nums)
    print("Sum: " + str(sum) + ", Product: " + str(prod))

    nums2 = [1, 2, 3, 4]
    sum, prod = array_sum_prod(4, nums2)
    print("Sum: " + str(sum) + ", Product: " + str(prod))
    
main()