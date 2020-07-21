# use of init method and defining and changing value of variable
class employee:

    def __init__(self):
        self.name="safi"
        self.age="30"

    def compare(self, other): # passing 2nd parameter as object
        if self.age==other.age:
            return True
        else:
            return False


emp1=employee()

emp2=employee()
emp2.age=25
if emp1.compare(emp2):
    print("They have same age")
else:
    print("They have different age")

