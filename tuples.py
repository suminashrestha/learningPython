# Tuples ->lets us create immutable sequence of values
tup = (2, 3, 4, 3)
# tup[0]=5  --> not allowed
print(tup)
print(type(tup))
print(tup[0])

# single value tuple -> comma is compulsory for it to be tuple
tup1 = (2,)
print(tup1)

# multiple value tuple -> comma is not necessary
# eg: tup2 = (2,3,5,6 ) and tup2=(2,3,5,6,) both acts as tuple

# Tuple methods
tupl = (2, 3, 4, 3, 3)
print(tupl.index(4))
print(tupl.count(3))
