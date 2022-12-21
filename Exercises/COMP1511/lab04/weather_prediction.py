NUM_TEMPS = 4
NUM_HUMIDITY = 5

def print_welcome():
    print("Hello and welcome to CS Weather!")
    print("=======================================")
    print("This program will help you to analyse a given weather patten")
    print("and make some predictions about the coming day")

def fill_array(size):
    array = [0.9] * size
    for i in range(size):
        array[i] = float(input())
    return array

def get_average(array, size):
    sum = 0.0
    for i in range(size):
        sum += array[i]
    return sum / size

def print_temp_statements(average_temp):
    print("The average temperature was: " + str("%.6f" % average_temp))
    if average_temp >= 28.0:
        print("It will be hot tomorrow!")
    elif average_temp >= 15.0 and average_temp < 28.0:
        print("Should be a lovely temperature tomorrow.")
    else:
        print("It'll be chilly tommorrow, pack a jumper!")

def print_humidity_statements(average_humidity):
    print("The average humidity was: " + str("%.6f" % average_humidity))
    if average_humidity > 80.0:
        print("It will be humid tomorrow.")
    else: 
        print("Shouldn't be too humid tomorrow.")
        

def main():
    print_welcome()
    
    print("Please enter the past " + str(NUM_TEMPS) + " day(s) worth of temperatures.")
    temps = fill_array(NUM_TEMPS)

    print("Please enter the past " + str(NUM_HUMIDITY) + " day(s) worth of humidities.")
    humidity = fill_array(NUM_HUMIDITY)

    print_temp_statements(get_average(temps, NUM_TEMPS))
    print_humidity_statements(get_average(humidity, NUM_HUMIDITY))
    
main()