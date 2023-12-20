#Day 1 11,15,10,6
#Day 2 10,14,11,5
#Day 3 12,17,12,4
#Day 4 15,21,22,4

import numpy as np

twoArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,4],[15,21,22,4]])
print(twoArray)

#Inserting values in the 2D array:
# newArray = np.insert(twoArray,1,[[1,2,3,4]],axis=0)
# print(newArray)

#Used to append the array in row wise at the last
newArray2 = np.append(twoArray,[[0,5,6,7]],axis=0)
print(newArray2)

#to add the new elements in column wise similar to append()
newArray1 = np.column_stack((twoArray,[1,2,3,4]))
print(newArray1)

#Accesing elements
def accessElement(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): #array[0] returns the length of columns
        print("Invalid inputs")
    else:
        print(array[rowIndex][colIndex])
        
accessElement(newArray2,0,1)

#traversal in two dimensional arrays
def traversalArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
traversalArray(newArray1)

#Searching the value in array
def searchElement(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"Found the {value} in {i} row and {j} column"
    return "Element not found!!"

print(searchElement(newArray1,97))

#Removing elements from 2D array ##creates a new array with the remaining elements
newTDarray = np.delete(newArray1, 1 , axis=0)
print(newTDarray)