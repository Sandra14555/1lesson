class Dog:
    def __init__(self, name="dog"):
        self.name = name


class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def print_dogs_names(self):
        if self.dogs:
            print(f"Names of {self.name}'s dogs:")
            for dog in self.dogs:
                print(dog.name)
        else:
            print(f"There are no dogs by {self.name}")



mars = Dog("Mars")
petya = Owner("Petya")

petya.add_dog(mars)

petya.print_dogs_names()

