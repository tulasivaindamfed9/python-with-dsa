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

# ______________________________________

# find the second largest element in the list
# using python in built function
list2=[1,4,8,6]
list2.sort(reverse=True)
second_largest=list2[1]
print("second largest element in the list: ",second_largest)
# _------------------------------

# another method to find the second largest element in the list
list2=[1,4,8,6]
maximum=0
for i in range(0,len(list2)):
    for j in range(i+1,len(list2)):
        if(list2[i]>list2[j]):
            maximum=list2[i]
            
            
#remove max element
list2.remove(maximum)
print("list2 after removing max element: ",list2)
# now we find the largest elemtn from this list to get the second largest element
second_largest=list2[0]
for i in range(1,len(list2)):
   if(list2[i]>second_largest):
            second_largest=list2[i]
print(second_largest)
           
       
   
           



