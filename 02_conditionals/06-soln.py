distance = int(input("What's the distance you want to cover:\n"))

if distance<3 :
    trans_mode ="Walk"
elif distance <=15:
    trans_mode="Bike"
else : 
    trans_mode="Car"

print(f"Transportation Mode should be : {trans_mode}")