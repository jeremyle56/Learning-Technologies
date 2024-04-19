
MAX_CARS = 20

class RaceResults:
    def __init__(self, car_number, race_time):
        self.car_number = car_number
        self.race_time = race_time

def race_results():
    cars = int(input("How many cars in the race? "))

    result = []
    for i in range(cars):
        if i == 0:
            print("Enter results: ")
        car_number, race_time = input().split()
        car_number = int(car_number)
        race_time = float(race_time)
        result.append(RaceResults(car_number, race_time))
    
    for i in range(cars):
        if i == 0:
            print("Results: ")
        print(f"{result[i].car_number}: {'%.2f' % result[i].race_time}")

race_results()