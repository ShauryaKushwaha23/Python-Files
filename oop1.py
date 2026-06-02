#object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex: phone, cup, book
#         You need a "class" to create many objects.

#class = (blueprint) used to design the structure and layout of an object.

from car import Car

car1 = Car("Mustang", 2025, "red", False)
car2 = Car("Corvette",2024, "black", True)
car3 = Car("Porsche", 2025, "Blue", True)

#car1.drive()
#car1.stop()
car1.describe()