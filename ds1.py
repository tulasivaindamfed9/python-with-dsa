# # reverse a list
# l1=[1,2,3,4,5]
# print(l1[::-1])

# # another method to reverse the list using for loop

# list1=[]
# for i in range(0,len(l1)):
#      n=len(l1)-1
#      list1.append(l1[n-i])
#      i=i+1

# print(list1)     

# l2=[]
# for i in range(0,5):
#     n=int(input("enter a number"))
#     l2.append(n)
# print(l2)
# print(l2[::-1])

# # -----------------------------

# # find largest and smallest element in the list
# l3=[9,6,0,4,8,4]
# largest=max(l3)
# smallest=min(l3)
# print(smallest,largest)

# another method to find the largest element in the list
# same method goes for smallest element just change the condition to l4[i]<l4[j] 
l4=[1,4,8]
# find larges element
# print(max(l4))

maximum=0
for i in range(0,len(l4)):
    for j in range(0,len(l4)):
        if(l4[i]>l4[j]):
            maximum=l4[i]
            
print("max value: ",maximum) 
