import numpy as np
import matplotlib.pyplot as plt

#in numpy elements start from 0 indexing 
a= np.array([(2,5,6,5),(2,3,4,5),(3,5,6,7)])
print(a[0,2])
print(a[0:,2])
print(a[0:2,2])

print(a.itemsize)
print(a.ndim)
print(a.dtype)
print(a.shape)

#only interchange row into columns
a = a.reshape(4,3)
print(a)


#a=np.linspace(1,3,5)

print(a.max())
print(a.min())
print(a.sum())

#1 axis is for rowns
print(a.sum(axis=1))

#0 axis is for columns
print(a.sum(axis=0))

print(np.sqrt(a))
print(np.std(a))

b = np.array([(2,4,5),(3,6,4)])
c = np.array([(2,3,4),(4,5,6)])

print(b+c)
print(b-c)
print(b*c)
print(b/c)

print(np.vstack((b,c)))
print(np.hstack((b,c)))

print(b.ravel())

#for plotting the elements on graph
x = np.arange(0,3*np.pi, 0.1)

#y = np.sin(x)
#y = np.tan(x)
y = np.cos(x)

plt.plot(x,y)
plt.show()
#############################################


ar=np.array([1,2,3])
print(np.log(ar))
print(np.log10(ar))
print(np.exp(ar))