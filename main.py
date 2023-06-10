import random
class killer:
    def __init__(self, name):
        self.name = name
        self.reputation = 50
        self.health = 0
        self.simulation = True

    def to_kill(self):
        print('Time to work')
        self.health -= 0.5
        self.reputation -= 10

    def to_sleep(self):
        print('i will sleep')
        self.health += 0.3

    def to_prepare(self):
        print('time to train')
        self.reputation += 5
        self.health += 0.5

    def is_alive(self):
        if self.health < -0.9:
            print('Oh, person who you fought with was stronger...')
            self.simulation = False
        elif self.reputation <= 0:
            print('In court they found out that you are a murderer...')
            self.simulation = False
        elif self.health and self.reputation > 5:
            print('You survived, and free,but you feel bad for what you did and you committed suicide')
            self.simulation = False

    def end_of_day(self):
        print(f'reputation = {self.reputation}')
        print(f'Progress = {self.health}')
    def live(self, day):
        day = "Day" + str(day) +" of " + self.name + " life. "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_kill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_prepare()
        self.end_of_day()
        self.is_alive()


lia = killer(name = "Lia")
for day in range(365):
    if lia.simulation == False:
        break
    lia.live(day)