score = int(input("Enter Your score: "))

if(score>=90 and score <=100):
    grade = "A"
    print("Grade is: " ,grade)
elif(score>=80 and score <=89):
    grade = "B"
    print("Grade is: " ,grade)
elif(score>=70 and score <=79):
    grade = "C"
    print("Grade is: " ,grade)
elif(score>=60 and score <=69):
    grade = "D"
    print("Grade is: " ,grade)
elif(score<=59 and score >= 0):
    grade = "F"
    print("Grade is: " ,grade)

else:
    print("Invalid Verify your Score")

