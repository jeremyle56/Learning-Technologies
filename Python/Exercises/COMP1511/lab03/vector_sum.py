class Vector():
    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;

def vector_sum(vector1, vector2):
    return Vector(vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z)
    
def main():
    x1, y1, z1 = input("Please enter the values of the first vector (x, y, z): ").split()
    x2, y2, z2 = input("Please enter the values of the first vector (x, y, z): ").split()
    first_vector = Vector(int(x1), int(y1), int(z1))
    second_vector = Vector(int(x2), int(y2), int(z2))

    sum_vector = vector_sum(first_vector, second_vector)
    print("The resulting sum vector is:")
    print(sum_vector.x)
    print(sum_vector.y)
    print(sum_vector.z)

main()