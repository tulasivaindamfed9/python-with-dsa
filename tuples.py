# # tuples indicated in () and are immutable

# tup1=(1,2,3,4,5)
# print(tup1)

# for i in tup1:
#     print(i)

# print(tup1[0]) # to access the first element of the tuple
# print(tup1[-1]) # to access the last element of the tuple
# print(tup1[1:3]) # to access the elements from index 1 to 2

# # concatenation of tuples
# tup2=(6,7,8,9,10)
# tup3=tup1+tup2
# print(tup3)

# tup4=tup3 + ("tulasi","sai")
# print(tup4)

# # we can only repeat the elements of the tuple but cannot change them
# tup5=tup1*2
# print(tup5)

# # inseting elements in tuple with user input and access particular element in tuple
# tup6=()
# n=4
# for i in range(0,n):
#     element=input("Enter the element: ")
#     tup6=tup6+(element,)
# print(tup6)

# # to access particular element in tuple
# print(tup6[1])

# find the index of an element(elephant) in a tuple
tup7=("cat","dog","rabbit","elephant","cat")
for i in range(0,len(tup7)):
    if tup7[i]=="elephant":
        print("the index is: "+ str(i))

# count the occurances of an element(cat) in a tuple   