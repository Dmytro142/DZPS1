import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 5
        self.progress = 3
        self.alive = True
    def to_study(self):
        print('Студент вчиться')
        self.gladness -= 3
        self.progress += 0.12
    def to_sleep(self):
        print('Студент заснув на парі')
        self.gladness += 2
        self.progress -= 1
    def to_chill(self):
        print('Студент грає в роблокс на парі')
        self.gladness += 4.5
        self.progress -= 0.12
    def to_eat(self):
        print('Студент поїв пельменів')
        self.gladness += 1.5
        self.progress += 0.1
    def late(self):
        print('Студент запізнився на пару')
        self.gladness -= 1.5
        self.progress -= 1.5
    def to_drink(self):
        print('Студент попив кави')
        self.gladness += 3.7
        self.progress += 2
    def to_grade(self):
        print('Студент заробив гарну оцінку')
        self.gladness += 2.5
        self.progress += 3
    def easy_question(self):
        print('Студенту дали легке питання')
        self.gladness += 3
        self.progress += 3
    def is_alive(self):
        if self.progress < -2:
            print('Студента відраховано')
            self.alive = False
        elif self.gladness <= 0:
            print('В студента депресія, його вигнали з гуртожитку')
            self.alive = False
        elif self.progress > 100:
            print('Студент втратив сенс навчання')
            self.alive = False
        elif self.gladness >100:
            print('Студент пішов з друзями до бару і напився')
            self.alive = False

    def end_of_the_day(self):
        print(f'щастя = {self.gladness}')
        print(f'Прогресс = {round(self.progress, 2)}')
    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' live'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 8)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.late()
        elif live_cube == 6:
            self.to_drink()
        elif live_cube == 7:
            self.to_grade()
        elif live_cube == 8:
            self.easy_question()
        self.end_of_the_day()
        self.is_alive()
baddenchik = Student(name= 'baddenchik')
for day in range(365):
    if baddenchik.alive == False:
        break
    baddenchik.live(day)