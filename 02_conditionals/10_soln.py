pet = input("Whats your pet : \n").lower()

if pet not in ("dog" , "cat"):
    print("Please enter correct Pet")
    exit()

Pet_age = int(input("What's your pet age?\n"))

# if pet =="dog":
#     if Pet_age < 2 :
#         food = "Puppy Food"
#     else:
#         food="Senior Dog Food"
# else:
#     if Pet_age < 2 :
#         food = "Puppy Food"
#     else:
#         food="Senior cat Food"

if Pet_age < 2 :
    food= "Puppy Food"
else:
    food=f"senior {pet} Food" 

print(f"Your {pet} needs {food}")