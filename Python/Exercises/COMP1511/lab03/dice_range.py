
def dice_range():
    sides = float(input("Enter the number of sides on your dice: "))
    num_die = float(input("Enter the number of dice being rolled: "))

    if sides <= 0 or num_die <= 0:
        print("These dice will not produce a range.")
        return

    print("Your dice range is " + str(int(num_die)) + " to " + str(int(sides * num_die)) + '.')
    print("The average value is " + str("{:.6f}".format((sides + 1) / 2 * num_die)))

dice_range()
