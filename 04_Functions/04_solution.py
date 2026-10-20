def area(radius):
    a = 3.14 * radius ** 2
    return a

def circum(radius):
    c = 2 * 3.14 * radius
    return c

radius = int(input("Enter radius: "))

print("__________________________________________________")


area_result = area(radius)
print("Area Result: ",area_result)

circum_result = circum(radius)
print("Circumference Result: ",circum_result)
print("__________________________________________________")