import numpy as np

n = np.array([[1,2,3],[4,5,6],[7,8,9]])#array
print(n)
print("\n")

n = np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin = 2)#ndmin = n dimension minimum
print(n)
print("\n")

n = np.array([[1,2,3],[4,5,6],[1,8,9]],dtype = complex)# data type
print(n)
print("\n")

dt = np.dtype(np.int32)# set data type
print(dt)
print("\n")

dt = np.dtype('i8')#1,2,4,8 as int 8,16,32,64
print(dt) 
print("\n")

dt = np.dtype([('age',np.int)])#creating your data type
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)
print("\n")

student = np.dtype([('name','S3'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
print("\n")
#'''b' − boolean ,'i' − (signed) integer ,'u' − unsigned integer,'f' − floating-point,
#'c' − complex-floating point,'m' − timedelta,'M' − datetime,
#'O' − (Python) objects,'S', 'a' − (byte-)string,'U' − Unicode,
#'V' − raw data (void)'''
