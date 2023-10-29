''' Point class which compares two points and returns true if they are equal and false if they are not equal.'''

class Point:

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"
    
''' Instantiate two points and compare them.'''
point1  = Point(1,2)
point2 = Point(1,3)
print(point1 == point2)