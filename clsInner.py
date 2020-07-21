class Student:

    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop: # inner class

        def __init__(self):
            self.brand='HP'
            self.cpu='i7'
            self.ram= 8

        def show(self):
             print(self.brand, self.cpu, self.ram)



s1=Student('safi', 2)
s2=Student('Farhin', 3)
Lap=Student.Laptop() # object for inner class
Lap.show() # calling inner class method
s1.show()
s2.show()
