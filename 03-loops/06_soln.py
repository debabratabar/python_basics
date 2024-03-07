num =int(input("Give me a number:\n"))
factorial=1
for i in range(num,1,-1):
    factorial*=i

print(f"Factorial of {num} is {factorial}")