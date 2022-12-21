import math

def print_pi():
    digits = input("How many digits of pi would you like to print? ")
    pi = [int(x) for x in str(math.pi).replace('.', '')]
    
    for i in range(int(digits)):
        print(pi[i], end = "")
        
        if i == 0:
            print(".", end = "")
    print()

print_pi()