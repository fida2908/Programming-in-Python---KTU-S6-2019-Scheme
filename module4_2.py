#Create a class Rectangle. A constructor is used to initialize the object values. Member function area() to compute the area of the rectangle

class Rectangle:
    def __init__(self,l=0,b=0):
        self.l = l
        self.b = b

    def area(self):
        print('Area: ',self.l*self.b)

R = Rectangle(1,2)
R.area()
