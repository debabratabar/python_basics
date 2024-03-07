password=input("Please enter your password:\n")
pass_len=len(password)
if pass_len <6:
    pass_condn="Weak"
elif pass_len<=10:
    pass_condn="Medium"
else:
    pass_condn="Strong"

print(f"Your password is {pass_condn}")