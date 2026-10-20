def kwarg(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

kwarg(name = "Atif",power = "Lazer")
kwarg(name = "Murtaza",power = "light")
kwarg(name = "Atif")