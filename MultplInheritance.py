# Multiple Inheritance
class A: # parent class or Super class
    def feature1(self):
        print("Class A Feature1 ")

    def feature2(self):
        print("Class A Feature2 ")

class B:  # Parent class or Super class
    def feature3(self):
        print("Class B Feature3")

    def feature4(self):
        print("Class B Feature4")

class C(A,B):
    def feature5(self):
        print("Class C Feature 5")

C1=C()
C1.feature2() # calling first parent class method
C1.feature4() # calling second parent class method
C1.feature5() # calling own method
