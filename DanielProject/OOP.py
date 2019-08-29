class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


class Teacher(person):

    def __init__(self, name='yoav', age=12, salary=10000):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return self.name, ' ', self.age, ' ', self.salary


class Student(person):

    def __init__(self, name='yoav', age=12, avg=85):
        person.__init__(self, name, age)

        self.avg = avg

    def __str__(self):
        return self.name, ' ', self.age, ' ', self.avg

    def get_avg(self):
        pass

    def set_avg(self):
        pass


prs1 = person()
tch1 = Teacher()
std1 = Student()
