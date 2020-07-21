# Single level inheritance
class A: # parent class or Super class
    def feature1(self):
        print("Class A Feature1 ")

    def feature2(self):
        print("Class A Feature2 ")

class B(A):  # child class or sub class
    def feature3(self):
        print("Class B Feature3")

    def feature4(self):
        print("Class B Feature4")


#A1=A()
#A1.feature1()
#A1.feature2()
B1=B() # calling parent class or super class method
# using child or sub class object
B1.feature1()
B1.feature2()
B1.feature3()
B1.feature4()