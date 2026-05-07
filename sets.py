# set is a collection of unique elements. if we enter repeated elements, 
# it takes only unique elements with the help of hashing
# sets are mutable and unordered and does not have any indexing. so we can't access elements  based on index
# {} is used to indicate sets
# we can add only immutable elements in sets. we can't add list in sets but we can add string and numbers
# sets are used to perform mathematical operations like union, intersection, difference and symmetric difference

# creating a set
set1=set()
# n=3
# for i in range(0,n):
#     element=input("Enter the element: ")
#     set1.add(element)

# print(set1) 

# adding tuple in set
set1.add((1,2,4))
print(set1) 