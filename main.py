import random
class Angel:
    def __init__(self, name):
        self.name = name
        self.kindness = 50
        self.progress = 0
        self.simulation = True

    def to_work(self):
        print('Time to work')
        self.progress += 0.5
        self.kindness -= 5

    def to_sleep(self):
        print('i will sleep')
        self.kindness += 3

    def to_chill(self):
        print('Rest time')
        self.kindness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Oh, you are the lowest angel...')
            self.simulation = False
        elif self.kindness <= 0:
            print('You were to sad,and now you can not work...')
            self.simulation = False
        elif self.progress > 5:
            print('Wow, now you are archangel!!!')
            self.simulation = False

    def end_of_day(self):
        print(f'Kindness = {self.kindness}')
        print(f'Progress = {self.progress}')
    def live(self, day):
        day = "Day" + str(day) +" of " + self.name + " life. "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_work()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


gabriel = Angel(name = "Gabriel")
for day in range(365):
    if gabriel.simulation == False:
        break
    gabriel.live(day)