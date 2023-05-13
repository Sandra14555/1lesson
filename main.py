import random
# class Human:
#     def __init__(self, name = "Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers!= []:
#             print(f"Names of {self.brand} passengers: ")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
# vasya = Human("Vasya")
# petya = Human("Petya")
#
# car = Auto("Mersedes")
#
# car.add_passenger(vasya)
# car.add_passenger(petya)
# car.print_passengers_names()
#______________SIMS____________________________
class Human:
    def __init__(self, name = "Human", job = None, home = None, car=None):
        self.name= name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

class Auto:
    pass
class House:
    pass
class Job:
    pass