class student:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other): # operator overloading of +
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self, other): # Operator overloading > gt method
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1> r2:
            return True
        else:
            return False

    def __str__(self): # operator overloading of _str_ method
        return '{} {}'.format(self.m1, self.m2)

s1=student(58,69)
s2=student(60,80)

s3=s1+s2
print(s3.m1)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")


a=9
print(a.__str__())

print(s1)