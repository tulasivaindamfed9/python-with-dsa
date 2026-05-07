# creating empty list and adding values to it using for loop and input function
list1=[]
n=5
for i in range(0,n):
    val=int(input("enter number  to add in list"))
    list1.append(val)
    
print("final list after taking values from user: ",list1) 

# accessing elements of list using indexing
for i in range(0,len(list1)):
    print("element at index ",i," is ",list1[i])

#directly printing the list elements
for i in list1:
    print(i) 

# reverse a list
print("reversed list: ",list1[::-1])    

list1.sort() # to sort the list in ascending order
print("sorted list in ascending order: ",list1)
list1.sort(reverse=True) # to sort the list in descending order
print("sorted list in descending order: ",list1)


