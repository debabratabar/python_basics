class Chai:
    origin = 'Indian'

print("## Class properties ##")
print(type(Chai))
print(Chai.origin)
Chai.is_good = True
print(Chai.is_good)


# creating object from Chai 
print("## object properties ##")
masala_tea = Chai()
print(type(masala_tea))
print(masala_tea.origin)
print(masala_tea.is_good)

masala_tea.origin='baloch'
masala_tea.is_good= 5

print('## after changing object value ##')
print(masala_tea.origin)
print(masala_tea.is_good)

print(Chai.origin)

print(Chai.is_good)



