weather = input("Enter your Weather: \n 1)Sunny \n 2)Rainy \n 3)Snowy \n Enter Here: ").upper()

if(weather == 'SUNNY' or weather==  "1"):
    print("Go for Walk")
elif(weather == 'RAINY' or weather== "2"):
    print("Read Book")
elif(weather == 'SNOWY' or weather == "3"):
    print("Build A Snowman")

else:
    print("check your syntax")