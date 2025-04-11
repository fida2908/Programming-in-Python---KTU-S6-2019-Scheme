#Define a class Mobile to store the details of a Mobile (company, model,price) with the following methods.
#   a) set_details()- to set the values to the data attributes
#   b)display_details()-to display the data attribute values

class Mobile:

    def set_details(self):
        self.company=input("enter compnay name: ")
        self.model=input("enter model name: ")
        self.price=float(input("enter price: "))

    def display_details(self):
        print(f'Company: {self.company}, Model: {self.model}, Price: {self.price}')
              
    
m = Mobile()
m.set_details()
m.display_details()


