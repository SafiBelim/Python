class computer: # creating class
    def config(self):
        print("i5, 16 GB, 1 TB HDD")


com1=computer() # creating object
com2=computer()
print(type(com1)) # it displays the type of object means class name
com1.config() # calling method of class using object
computer.config(com2) # another method to calling method of class using object
print()