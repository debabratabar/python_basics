user_score = int(input("Enter your score : \n" ))

if  user_score > 100 or user_score < 0 :
    print("Please Enter correct score ")
    exit()

if user_score >= 90 :
    Grade = 'A'
elif user_score >= 80 :
    Grade = 'B'
elif user_score >= 70 :
    Grade = 'C'
elif user_score >= 60 :
    Grade = 'D'
else:
    Grade = 'F'

print( f"Your grade is : {Grade}")
