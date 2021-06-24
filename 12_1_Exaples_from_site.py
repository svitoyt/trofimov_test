# Different types of sets in Python
# set of integers
test_set = {5, 3, 4, 2, 1}
print('1:', test_set)

# set of mixed datatypes
test_set_1 = {5.5, "Andrey Trofimov", (3, 2, 1)}
print('2:', test_set_1)

# set cannot have duplicates
test_set_2 = {7, 7, 3, 4, 3, 4}
print('3:', test_set_2)

# we can make set from a list
test_set_3 = set([5, 6, 3, 6])
print('4:', test_set_3)

# initialize my_set
test_set_4 = {2, 6}
print('5:', test_set_4)

# add element into the set
test_set_4.add(3)
print('6:', test_set_4)

# add multiple elements
test_set_4.update([5, 7, 8])
print('7:', test_set_4)

# add list and set
test_set_4.update([3, 5], {2, 7, 11})
print('8:', test_set_4)

# discard an element
test_set_4.discard(6)
print('9:', test_set_4)

# remove an element
test_set_4.remove(8)
print('10:', test_set_4)

# initialize my_set
# Output: set of unique elements
test_set_5 = set("LondonIsACapital")
print('11:', test_set_5)

# pop an element
# Output: random element
print('12:', test_set_5.pop())

# pop another element
test_set_5.pop()
print('13:', test_set_5)

# clear my_set
# Output: set()
test_set_5.clear()
print('14:', test_set_5)

# Set union method
a = {1, 3, 3, 2, 5, 6, 9}
b = {4, 6, 6, 7, 8, 9}
print('15:', a|b)
print('16:', a.union(b))
print('17:', b.union(a))

# Intersection of sets
print('18:', a & b)
print('19:', a.intersection(b))
print('20:', b.intersection(a))

# Difference of two sets
print('21:', a - b)
print('22:', a.difference(b))
print('23:', b - a)
print('24:', b.difference(a))

# Symmetric difference of two sets
print('25:', a ^ b)
print('26:', a.symmetric_difference(b))
print('27:', b.symmetric_difference(a))


