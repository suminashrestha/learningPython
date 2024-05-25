'''
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
'''

f = open("demo.txt", "r")
# data = f.read()  # if we do this in the beginning, we cannot do
# print(data)      #readline() after it

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)


f.close()
