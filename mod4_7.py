 # Write a Python class which has two methods get_distance and print distance. get distance accept a distance in kilomefres from the user and print_distance print the distance in meter.

class Distance:
    def get_distance(self):
        self.dist = int(input("Enter the distance in kilometer: "))

    def print_distance(self):
        print(f"Distance: {self.dist}")

d = Distance()
d.get_distance()
d.print_distance()
        