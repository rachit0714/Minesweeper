import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, p2):
        return math.sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)

    def tuppulate(self):
        return (self.x,self.y)

    def __str__(self):
        return f"(({self.x} , {self.y}))"
