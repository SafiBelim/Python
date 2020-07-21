f = open('MyData.txt','r')
# to open file for reading as r
#print(f.readline(), end='') # for reading
#print(f.readline())

f1 = open('abc','w') # for writing w and appending a for reading r ,
#f1.write('Laptop')


# copying one file to another
for data in f:
    f1.write(data)
