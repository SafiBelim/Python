class car:

    wheels = 4 # class variable
    def __init__(self):
        self.mil = 80  # instance variable
        self.comp = "BMW"



c1=car()
c2=car()
c2.mil=90
# i.e. static variable it changes the value of all objects...
print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c1.wheels)