animal_name = input(("Enter the animal name: \n 1) Dog \n 2) Cat \n ")).lower()

if(animal_name == "dog" or animal_name == '1'):
    food = "Puppy Food"
elif(animal_name == 'cat' or animal_name == '2'):
        food = "Seniour Cat food"

print(food)