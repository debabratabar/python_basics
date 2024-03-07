fruit_name = input("Enter the Fruit Name : \n ")
if fruit_name.lower() != "banana" :
    print("Please enter correct Fruit Name\n")
    exit()

fruit_color = input("Enter the Fruit color : \n").lower()



if fruit_color == "green" :
    fruit_condn= "Unripe"
elif fruit_color  == "yellow":
    fruit_condn="Ripe"
elif fruit_color == "brown":
    fruit_condn = "Overripe"
else:
    print("Please enter correct fruit Color")
    exit()

print(f"Your {fruit_name} is {fruit_condn}")

