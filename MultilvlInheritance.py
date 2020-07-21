# Multi level Inheritance
class A: # Grand parent class or Super class
    def feature1(self):
        print("Class A Feature1 ")

    def feature2(self):
        print("Class A Feature2 ")

class B(A):  # Parent class
    def feature3(self):
        print("Class B Feature3")

    def feature4(self):
        print("Class B Feature4")

class C(B): # Child class
    def feature5(self):
        print("Class C Feature 5")


C1=C() # creating child class object
C1.feature1() # calling all methods using child class object
C1.feature3()
C1.feature5()
