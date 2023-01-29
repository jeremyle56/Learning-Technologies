class Player:
    def __init__(self, name) -> None:
        self.name = name

class Chair:
    def __init__(self, name) -> None:
        self.sitting = Player(name)
        self.next = None

def make_music(turns, chairs):
    for i in range(turns):
        curr = chairs
        unseated = None
        while curr:
            moving = curr.sitting
            curr.sitting = unseated
            unseated = moving
            curr = curr.next
        if chairs:
            chairs.sitting = unseated
    
    beheaded = chairs
    print(beheaded.sitting.name)
    chairs = chairs.next

    return chairs

def be_seated(name, heir):
    c = Chair(name)
    c.next = heir
    return c

def main():
    thrones = be_seated("Robert Baratheon", None)
    thrones = be_seated("Cersei Lannister", thrones)
    thrones = be_seated("Joffrey Baratheon", thrones)
    thrones = be_seated("Eddard Stark", thrones)
    thrones = be_seated("Spoiler Alert", thrones)
        
    thrones = make_music(1, thrones)
    thrones = make_music(3, thrones)
    thrones = make_music(0, thrones)
    thrones = make_music(2, thrones)

main()
