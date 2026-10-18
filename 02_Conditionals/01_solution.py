age  = int(input("Enter your age: "))

if(age>= 0 and age<13):
    print("Your are Child")
elif(age>=13 and age<=19):
    print("You are Teenager")
elif(age>=20 and age<=59):
    print("You are Adult")
elif(age>=60 and age<=100):
    print("You are Seniour")
else:
    print("Please Enter Correct Age")