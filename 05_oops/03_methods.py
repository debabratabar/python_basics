class Chai:
    origin = 'Indian'

    def origin_print(self):
        print(f'the origin of the chai is {self.origin}')


Chai.is_good = True

# creating object from Chai 
print("## object properties ##")
masala_tea = Chai()
masala_tea.color = 'black'
print(type(masala_tea))
print(masala_tea.origin)
print(masala_tea.is_good)
print(masala_tea.color)


# atrribute shadowing 
del masala_tea.color
try:
    print(masala_tea.color)
except Exception as e :
    print("########## ERROR ############")
    print(e)
    print("########## ERROR ############")


# self argument

masala_tea.origin_print() # method calling  using object 
Chai.origin_print(masala_tea) # another way of calling methods 






