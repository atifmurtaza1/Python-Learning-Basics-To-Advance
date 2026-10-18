fruit = input("Enter Fruit name Banana and Apple only: ").upper()
color = input('Enter Color name: ').upper()

if(fruit == 'BANANA'):
    if(color=='GREEN'):
        print("Its Unripe:")
    elif(color == 'YELLOW'):
        print("Its Ripe")
    elif(color == 'BROWN'):
        print("Its Over Ripe")
    else:
        print("Verify the syntax")


if(fruit == 'APPLE'):
    if(color=='GREEN'):
        print("Its Unripe:")
    elif(color == 'YELLOW'):
        print("Its Ripe")
    elif(color == 'BROWN'):
        print("Its Over Ripe")
    else:
        print("Verify the syntax")
else:
    print("Check your syntax")
        