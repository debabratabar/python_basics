str = input("Give me a string: \n")
reverse_string=''

for i in range ( len(str)-1 , -1 , -1):
    reverse_string+=str[i]

print(reverse_string)

