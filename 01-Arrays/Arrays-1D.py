from array import *

#Creating an array
arr1 = array("i",[1,2,3,4,5,6,7,8,9,10])

#traversal thru an array
for i in arr1:
    print(i)
    
#append(): used to insert element at the end
arr1.append(11)
print(arr1)

#Extend array
arr2 = array("i", [12,13,14,15,16])
arr1.extend(arr2)

#fromlist(): used to add items from list into array
a = [22,33,44,55]
arr1.fromlist(a)

#remove(): used to remove an element from an array from the first occurance
arr1.remove(11)

#pop(): used to remove the last element of an array
arr1.pop()

#index(): used to find the index of any values
arr1.index(3)

#reverse(): used to reverse the array
arr1.reverse()

#count(): used to count the occurances of each element in array
arr1.count(11)

#tolist(): used to convert the array to list
arr1.tolist()

#slicing elements in array
arr1[1:4]