# Constructor calling in Inheritance
class a:
    def __init__(self):
        print("Contructor of a")

    def Feature1(self):
        print("class a Feature 1")

class b(a):
    def __init__(self):
        print("consructor of b")
        super().__init__() # to call constructor of super class

    def Feature2(self):
        print("class b Feature 2")

b1=b() # by default it call it self class constructor but not super class
b1.Feature1()
b1.Feature2()