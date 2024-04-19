from enum import Enum

MIN_YEAR = 1900

class Zodiac(Enum):
    RAT = 0
    OX = 1
    TIGER = 2
    RABBIT = 3
    DRAGON = 4
    SNAKE = 5
    HORSE = 6
    GOAT = 7
    MONKEY = 8
    ROOSTER = 9
    DOG = 10
    PIG = 11

birth_year = int(input("Enter the year of your birth: "))
birth_year = (birth_year - MIN_YEAR) % 12
print(Zodiac.RAT.value)

if birth_year == Zodiac.RAT.value:
    print("You were born in the year of the Rat!")
elif birth_year == Zodiac.OX.value:
    print("You were born in the year of the Ox!")
elif birth_year == Zodiac.TIGER.value:
    print("You were born in the year of the Tiger!")
elif birth_year == Zodiac.RABBIT.value:
    print("You were born in the year of the Rabbit!")
elif birth_year == Zodiac.DRAGON.value:
    print("You were born in the year of the Dragon!")
elif birth_year == Zodiac.SNAKE.value:
    print("You were born in the year of the Snake!")
elif birth_year == Zodiac.HORSE.value:
    print("You were born in the year of the Horse!")
elif birth_year == Zodiac.GOAT.value:
    print("You were born in the year of the Goat!")
elif birth_year == Zodiac.MONKEY.value:
    print("You were born in the year of the Monkey!")
elif birth_year == Zodiac.ROOSTER.value:
    print("You were born in the year of the Rooster!")
elif birth_year == Zodiac.DOG.value:
    print("You were born in the year of the Dog!")
else:
    print("You were born in the year of the Pig!")

