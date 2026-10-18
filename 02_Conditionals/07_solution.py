order_size = input("Enter Size of Coffe:\n 1) Small \n 2) Medium \n 3) Large \n ")
extra_shot = input("Extra shot \n 1) Yes \n 2) No \n").lower()

if(extra_shot == 'yes' or extra_shot == '1'):
    coffee = order_size + " Wit Extra Shot"
else:
    coffee = order_size + " With Coffee"

print('Order: ', coffee)