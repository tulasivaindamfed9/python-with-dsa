# dictionary is a collection of key-value pairs. it is mutable and unordered. it is represented by {} and key-value pairs are separated by : and each pair is separated by ,
# keys are unique and immutable. values can be of any data type and can be duplicated.
# only immutable data types are allowed as keys in a dictionary. we can use string, numbers and tuple as keys but we can't use list or set as keys in a dictionary
# we can have same value for diff keys but not same key for diff values in a dictionary
# dictionary can be converted to list and tuple using list() and tuple() functions respectively. when we convert a dictionary to list or tuple, only the keys are converted to list or tuple and values are not included in the list or tuple
dict1={
    1:"ram",
    2:"sita",
    3:"shiv",
    "wife of shiv":"parvathi",
    "shiv son's":["ganesh","shanmukh"]
}  
print(dict1)
dict1["ram bro"]="lakshman"
print(dict1)
print("keys of dict1: ",dict1.keys())
print("values of dict1: ",dict1.values())

# to get particular key value
print(dict1.get(1))

# to convert dict to list
print(list(dict1)) # it will convert only keys of dict to list
print(list(dict1.items())) # it will convert dict to list of tuples where each tuple is a key-value pair


# update method to update some more key-value pairs to an existing list
dict2={
    "om":"shanti om",
    "namo":"narayanaya"
}
dict1.update(dict2)
print(dict1)        