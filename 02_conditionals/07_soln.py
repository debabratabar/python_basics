coffee_size = input("Whats your coffee size:\n")
extra_shot =input("Do you need extra shot(Y/N)?:\n")

if extra_shot.lower() == "y":
    print(f"Here is your {coffee_size} coffee with extra shot")
else:
    print(f"Here is your {coffee_size} Coffee")
