print("-------------Password Strength Checker-------")
password = input("Enter Your Password:")

if(len(password) < 6 and len(password)> 0):
    strength = "Weak"
elif(len(password) > 6 and len(password) < 10):
    strength = "Medium"
elif(len(password)>= 10):
    strength = "Strong"
else:
    ("Check your Paswwrod")
print("Password strenght is: " + strength)