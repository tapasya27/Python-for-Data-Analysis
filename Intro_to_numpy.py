import numpy as np

data = np.random.randn(2, 3) #2 rows, 3 columns 

data2 = np.arange(4)  #1 row with 10 elements

print(data)
print(data2)
print(data.shape)  #To find the shape
print(data.dtype)  #To find datatype

#to create an a single ndarray -  use the function array on a list 

list1 = [1, 4, 6.8, 1]
arr1 = np.array(list1)   #np.array takes a sequence in as an input 
print(arr1)

#multidimensional arrays - give input as nested lists 

multi_lists = [[4,5,2,6],[1,2,4,6.7]]
multi_arr = np.array(multi_lists, dtype=np.float64)
print("This is a", multi_arr)
print("Dimension of this array is", multi_arr.ndim) #an array inside an array is 2D, gives nu. of rows


#creating special arrays 
print(np.zeros(10))  #1D array of 10 zeroes 
print(np.zeros((3,6))) #2D array with 6 columns and 3 rows
print(np.empty((2,3,2)))  #empty helps to create an array without setting the entries 
print(np.arange(15)) #creates an ndarray from 0 to 14 
print(np.eye(4)) #creates an identity matrix of dimensions 4x4 or np.identity()

#typecasting 
#string numbers can also be typecasted to actual numbers 
float_arr = arr1.astype(np.float64)
print(float_arr)

print("Comparing arrays here")
print(arr1>data2)

#important note, slice is a view of an original array. Any important modification to the slice will also take place with the array
arr_toslice = np.arange(15)
print(arr_toslice[10])

arr_toslice[5:8] = 67

print(arr_toslice)

arr_toslice[5:8].copy() #to create a copy instead of a slice 

print(multi_arr)
print(multi_arr[0][3]) #should print 6