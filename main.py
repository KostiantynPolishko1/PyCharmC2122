class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')

# personX = Person(name='Kostiantyn', surname='Polishko', age=30)
# personX.info_person()

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

polishko = Teacher(subject='Pycharm', hours=24, name='Kostiantyn', surname='Polishko', age=30)
# polishko.info_all()
