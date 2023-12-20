import array

my_array = array.array("i") #creates an empty array
my_array1 = array("i", [1,2,3,4,5]) #creates an array with values

# import numpy as n
# np_array = n.array([], dtype=int)
# np_array_1 = n.array([1,2,3,4,5],dtype=int)

#Time complexity
#O(1) : for creating an empty array using array module
#O(1) : for creating an empty array using numpy
#Space Complexity also remains same

#Time Complexity and Space Complexity
#O(n) : for both array modules and numpy modules

#Insertion
arr1 = array("i",[1,2,3,4,5])
arr2 = array("d",[1.3,1.4,1.5,1.6])

arr1.insert(5,9) #index:5 and value:9

#Traversal
def traversal(arr1):
    for i in arr1:
        print(i)
        
traversal(arr1)

#Accesing an element in array
def accessElement(array,index):
    if index > len(array):
        print("Array is out of bound")
    else:
        print(array[index])
        
#Searching for an element
def searchElement(array,value):
    for i in range(len(array)):
        if array[i] == value:
            print(f"Element is found at the index:{i}")
        else:
            print("Value not found")