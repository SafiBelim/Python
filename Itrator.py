class Topten:
    def __init__(self):
        self.num=1

    def __iter__(self): # defining iter class object
        return self

    def __next__(self): # defining next of itrator
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration # raising exception


values = Topten()

#print(next(values))# itrator method calling so
# in next in for loop it print from 2 no only because using iterator
for i in values: # built in for loop iterator call iter method which we have override
    print(i)