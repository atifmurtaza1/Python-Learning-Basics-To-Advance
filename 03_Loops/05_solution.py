text  = input("Enter the string to : ")

for i in text:
    if text.count(i) == 1:
        print("character is: ", i)
        break
    