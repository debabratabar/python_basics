n = int(input("Enter a number=\n"))
sum_of_even_nuumbers = 0
for i in range(n):
    if i%2==0:
        sum_of_even_nuumbers+=i

print(f"sum of even numbers ={sum_of_even_nuumbers}")