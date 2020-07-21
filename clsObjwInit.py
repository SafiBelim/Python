class computer:
    def __init__(self, cpu, ram):# creating init method
        # which works as initializer of class
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("computer configuration is", self.cpu,self.ram)



com1=computer("i5",16)
com2=computer("atom",8)
com1.config()
com2.config()