#Create a class car with attributes model, year and price and a method cost() for displaying the prize. Create two instance of the class and call the method for each instance.(university question)

class car:
    def __init__(self,model,year,prize):
        self.model = model
        self.year = year
        self.prize = prize

    def cost(self):
        print('Prize: ',self.prize)

c1 = car('Maruti',1997,200000)
c2 = car('Ford',2015,500000)  

c1.cost()
c2.cost()

        