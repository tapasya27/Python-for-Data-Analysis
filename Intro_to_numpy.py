import numpy as np

data = np.random.randn(2, 3)

print(data.shape)  #To find the shape
print(data.dtype)  #To find datatype

#to create an a single ndarray -  use the function array on a list 

list1 = [1, 4, 6.8, 1]
arr1 = np.array(list1)
print(arr1)

#multidimensional arrays - give input as nested lists 

multi_lists = [[4,5,2,6],[1,2,4,6.7]]
multi_arr = np.array(multi_lists)
print("This is a", multi_arr)
print("Dimension of this array is", multi_arr.ndim) #an array inside an array is 2D


#creating special arrays 
print(np.zeros(10))  #1D array of 10 zeroes 
print(np.zeros((3,6))) #2D array with 6 columns and 3 rows
print(np.empty(2,3,2))  #helps to create an array without setting the entries 




