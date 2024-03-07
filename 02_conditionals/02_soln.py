import datetime
age = int(input("Enter your age : \n"))

# getting today Day 
today_date = datetime.datetime.now()
today = today_date.strftime("%A")

price = 12 if age >=18 else 8


if today == "Wednesday":
    price -=2

print(f"Your Movie ticket price : {price} ")
