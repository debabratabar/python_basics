class BaseChaiClass:

    def __init__(self , type_):
        self.type = type_

    def prepare(self):
        return f'preparing {self.type} chai '
    

# example of inheritance    
class Masalachai(BaseChaiClass):

    def add_spice(self ):
        return f'Adding masala for {self.type} chai '


# example of composition , not directly inheriting , but taking a reference 

class ChaiShop:
    chai_cls = BaseChaiClass 

    def __init__(self):
        self.chai = self.chai_cls('Cutting')
    
    def serve(self):
        print(self.chai.prepare())
        print(f'servring {self.chai.type} Chai ')
        
# example of composition and inheritance 
# getting intialize using chaishop , which has ref of BaseChaiClass 
# and having ref of Masalachai also , it can access prepare , serve , add_spice 
class NewChaiShop(ChaiShop):
    chai_cls = Masalachai
    # pass
    

mchai = Masalachai('cardamom')

print(mchai.type)
print(mchai.prepare())
print(mchai.add_spice())

print("###################")

shop = ChaiShop()

shop.serve()

print("###################")
shop_2 = NewChaiShop()

# shop.serve()
shop_2.chai.add_spice()

shop_2.chai.prepare()
shop_2.serve()
