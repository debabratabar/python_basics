class ChaiOrder:

    # constructor 
    
    def __init__(self  , name , price ):
        self.name = name 
        self.price  =price 
        # return 1 

    def __init__(self  , name , price=100 ):
        self.name = name 
        self.price  =price 
        # return 1

   


    def printName(self):
        return f'The chai name is {self.name}'
    
    def printPrice(self):
        return f' the price of the {self.name} is {self.price}'
    


masala_chai = ChaiOrder('Masala' , 20)

print(masala_chai.printName())
print(masala_chai.printPrice())



ulong_chai = ChaiOrder('Masala' )

print(ulong_chai.printName())
print(ulong_chai.printPrice())
