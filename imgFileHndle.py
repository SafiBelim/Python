# copying image file
f = open('header.jpg','rb') # read binary rb

f1 = open('Rightway.jpg','wb')

for i in f:
    f1.write(i)