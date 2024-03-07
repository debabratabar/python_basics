year = int(input("Enter an year:\n"))

if (year%400 ==0) or (year%4 ==0 and year%100 !=0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")