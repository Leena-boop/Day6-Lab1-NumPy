#Leena alhabrdi 

import numpy as np
#Q#1: Create x array with elements equal to 1.
x = np.ones([4,4])
#Q#2: Create y array with elements equal to 0.
y = np.zeros([4,4])
#Q#3: Add x and y arrays.
x+y

#Q#4: Print x array characteristics (e.g: dimension, shape, size, type)
x.shape
x.size
type(x)
len(x)

# Create a 2D array "called w" as the following
w = np.array([[11,12,13] , [14,15,16]])
##6: Create z array contains the numbers from 1 to 3
z = np.arange(1,4)

#Q#7: Combine the arrays z and w in vertical way then save it in a new variable "newArray".
newArray = np.vstack((z,w))

#Q#8: Print all elements of "newArray" using the loop
for row in newArray:
    for item in row:
      print(item)
  

#Q#9: Reverse the columns and rows of "newArray".
newArray.transpose()

#Q#10: Decrement all elements of "newArray" with 1
newArray +=1

#Q#11: Find smallest and biggest values in "newArray".
#smallest
newArray.min()
#biggest
newArray.max()

#12: Print the first row of "newArray" using indexing.
print(newArray[0])
#13: Print the number equals 12 of "newArray" using indexing.
print(newArray[newArray == 12])
#14: Print the numbers equal 0 and 13 of "newArray" using Slicing.
print(newArray[[0,2], 0:1])
#15: Change the shape of "newArray" to (9,1).
v =newArray.reshape(9,1) 
print(v)

#16: Change the shape of "newArray" to (3,2).
#newArray.reshape(3,2) -- can not implement