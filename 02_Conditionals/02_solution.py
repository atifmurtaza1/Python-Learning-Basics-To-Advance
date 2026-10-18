age = int(input("Enter Your age: "))
days = input("Enter the day of the week \n 1-Wednesday \n 2-Other Day: ").upper()

price = 12 if age >= 18 else 8

if(days == "WEDNESDAY" or days == "1"):
    price -= 2
    print("Ticket Price with discount is: ", price)
else:
    print("Ticket price is: ", price)

