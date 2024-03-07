str = input("Give me a string:\n")

for i in str:
    if str.count(i)==1:
        print(f"first Non-repeated Character is {i}")
        exit()

print("There is no non-repeted character ")