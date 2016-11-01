class Monkey:
    __abc='hello'

    def __init__(self):
        self.name='Abc'
        self.age=20
    def drink(self):
        print(self.name +str(self.age),Monkey.__abc)

    @staticmethod
    def get_eat():
        return Monkey.__abc

t=Monkey()

t.drink()
#t.eat()
#t.__salary=5000
#print(t.change_salary())
