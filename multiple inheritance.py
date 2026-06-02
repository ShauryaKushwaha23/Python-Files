#multiple inheritance = Inherit from more than one parent class
#                       C(A, B)

#multilevel inheritance = Inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A

class Animal:
    def eat(self, name):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")




