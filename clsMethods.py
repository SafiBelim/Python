class Student:
    school = "Rightway School"

    def __init__(self, m1, m2, m3):  # instance method which has instance as parameter
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod  # class method which has class as parameter
    def get_school(cls):
        print(cls.school)

    @staticmethod
    def get_schoolInfo():  # static method which neither class nor class as parameter
        print("It's Rightway primary School")


s1 = Student(65, 85, 74)
print(s1.avg())  # calling instance method
Student.get_school()  # calling class method
Student.get_schoolInfo()  # calling static method
