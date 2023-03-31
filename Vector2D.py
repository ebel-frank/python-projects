import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y

    def __truediv__(self, other):
        return Vector2D(self.x/other.x, self.y/other.y)

    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)

    def nomalized(self):
        length = self.getLength()
        if length != 0:
            return Vector2D(self.x/length, self.y/length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y,self.x))

    def __str__(self):
        return "X: " + str(self.x) + ",Y: " + str(self.y)
        
def Main():
    vec = Vector2D(5, 6)
    vec2 = Vector2D(2, 3)
    print(vec)
    print(vec2)

    tempmethod = vec.getAngle    

    vec = vec + vec2
    print(vec)
    
    vec = vec + vec2
    print(vec)
    
    vec = vec * Vector2D(2, 2)
    print(vec)
    
    print(vec.nomalized())
    print(vec.getAngle())
    tempmethod2 = vec.getAngle

    print(tempmethod(), " and ",tempmethod2())

if __name__=="__main__":
    Main()
    
