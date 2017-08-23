import numpy as np

'''
# 1d array
a = np.array([1,2,3])

print(a)
'''

'''
# 2d array
a = np.array([(1,2,3),(4,5,6)])

print(a)
'''

'''
#why we use numpy instead of list
#lets see

import time

import sys

#list
s = range(1000)

print(sys.getsizeof(7) * len(s))

#using numpy array
#arange works same like range but on numpy
t = np.arange(1000)

print(t.size * t.itemsize)
'''

'''
import time

import sys

size = 10000000

#for list
l1 = range(size)
l2 = range(size)

start = time.time()

result = [(x,y) for x,y in zip(l1,l2)]

print((time.time()-start) * 1000)

#for numpy
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

result = a1+a2

print((time.time()-start) * 1000)
'''


a = np.array([(1,2,3,4,5,6),(2,3,4,7,8,9)])

'''
print(a.ndim) #dimension of array

print(a.itemsize) #size of item

print(a.dtype) #data type of array

print(a.size) #size of array

print(a.shape) #2 rows, 6 columns
'''

'''
print(a)

#reshaping to 6 rows, 2 columns
a = a.reshape(6, 2)

print (a)
'''

'''
print(a[0,2]) #0th element index 2

print(a[0:,3]) #0 in both the element with index 3
'''

'''
#line spacing
a = np.linspace(1,3,10)

print(a)
'''

'''
a = np.array([1,2,3])

print(a.max())

print(a.min())

print(a.sum())
'''


#a = np.array([(1,2,3),(3,4,5)])

#b = np.array([(1,2,3),(3,4,5)])

'''
print(a.sum(axis=0)) #sum of axis 0

print(a.sum(axis=1)) #sum of axis 1

print(np.sqrt(a)) #sprt of each element

print(np.std(a)) #standard deviation = how much the members of the group
                 # differ from the mean value of group
'''

'''
print(a+b) #sum of matrix

print(a-b) #diff of matrix

print(a*b) #mult of matrix

print(a/b) #div of matrix
'''

#print(np.vstack((a,b))) #vertical stacking

#print(np.hstack((a,b))) #horizontal stacking

#print(a.ravel()) #a matrix in single column


'''
#ploting of sin and cos funtion using matplotlib

import matplotlib.pyplot as plt

#for sin
x = np.arange(0,3*np.pi, 0.1)

y = np.sin(x)

plt.plot(x,y)

plt.show()

#for cos
x = np.arange(0,3*np.pi, 0.1)

y = np.cos(x)

plt.plot(x,y)

plt.show()

#for tan
x = np.arange(0,3*np.pi, 0.1)

y = np.tan(x)

plt.plot(x,y)

plt.show()
'''

'''
#exponential and logarithmic function

import matplotlib.pyplot as plt

ar = np.array([1,2,3])

print(np.exp(ar)) #exponent

print(np.log(ar)) #natural log

print(np.log10(ar)) #natural log
'''

