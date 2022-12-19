
hello, hola = 'hi mom', 'hola mamá';

my_tuple = ('a', 'b')

my_list = [1, 2, 3]

my_dict = {
    'key' : 'value'
}

def have_fun():
    for i in range(5):
        print(i)

map(lambda x: x * 2, my_list)

class Reptile:
    def __init__(self, length):
        self.length = length

class Snake(Reptile):
    def slither(self):
        print("I'm a snake 🐍")