distance = int(input("Enter the Kilo meter: "))

if(distance < 3 and distance > 0):
    transport = "Go By Walk"
elif(distance >=3 and distance <= 15):
    transport = "Go by Bike"
elif(distance > 15):
    transport = "Go By Car"
else:
    print("Check the value")
    exit()

print(transport)