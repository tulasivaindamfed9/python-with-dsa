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


# find missing number in a set of consecutinve numbers
set2={1,3,4}
def find_missing_num(nums):
    # convert set to list and sort the list
    nums=sorted(nums)
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if(nums[j]-nums[i]!=1):
                miss=nums[j]-nums[i]
                return miss
                
print(find_missing_num(set2))


# find all  the pairs of elements in the given set which has a diff of 4
set3={2,5,9,4,8,12}
def df4pair(nums):
    nums=list(nums)
    pairs=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            # abs means absolute value. it returns the positive value of the difference between two numbers
            if abs(nums[i]-nums[j]) == 4:
                pairs.append((nums[i],nums[j]))
    
    return pairs
print(df4pair(set3) )