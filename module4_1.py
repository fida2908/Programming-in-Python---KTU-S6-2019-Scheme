#Create class Arith to do arithmetic operation. It contains a member function read()
#to read the two numbers and add() method to find the sum. You can add more
#methods to the class to incorporate more functionality.


class Arith:
    def read(self):
        self.x = int(input('Enter number 1: '))
        self.y = int(input('Enter number 2: '))

    def add(self):
        print('Sum: ',self.x + self.y)

A = Arith()
A.read()
A.add()