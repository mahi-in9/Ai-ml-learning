# Dunder Method

class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector{self.x}, {self.y}"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    def __len__(self):
        return 2;

v1 = Vector(1, 2);
v2 = Vector(3, 5);

print(v1)
print(v1 + v2)
print(v1 * 3)
print(len(v2))