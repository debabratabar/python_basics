num = int(input("Give me a number : \n"))

isPrime = True 

for i in range(2,num):
    if num%i==0:
        isPrime=False
    
if isPrime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")