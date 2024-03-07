weather = input("What's the Weather now ?\n").lower()

if weather == "sunny":
    activity = "Go for a Walk"
elif weather == "rainy" :
    activity ="Read a book"
elif weather== "snowy":
    activity = "Build a snowman"
else:
    print("Please enter corrent weather condition")
    exit()

print(f"You can {activity}")
