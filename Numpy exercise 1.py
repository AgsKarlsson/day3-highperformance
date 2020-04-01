import numpy as np

#Speaking of efficient programs, it's not very 
#efficient to run all of the excercises again and again
#as I'm working on this... Oh well 

#part a
a=np.zeros(10)
a[4]=1
#print(a)

#part b
b=np.arange(10,50,1)
#print(b)

#part c
revb=b[::-1] #I don't understand why two : are needed here when b is 1D...
#print(revb)

#part d
d=np.arange(9).reshape((3,3))
#print(d)

#part e
e=np.array([1,2,0,0,4,0])
enz=np.nonzero(e)
#print(enz)

#part f
f=np.random.random_sample([30])
fmean=np.mean(f)
#print(fmean)

#part g
g=np.ones([3,3])
g[1,1]=0
#print(g)

#part h
h=np.zeros([8,8])
h[0:8:2,0:8:2]=1
h[1:8:2,1:8:2]=1
#print(h)

#part i
ia=np.array([[1, 0], [0, 1]])
i=np.tile(ia, (4,4))
#print(i)

#part j
j=np.arange(11)
j=np.delete(j, np.argwhere( (j>2)&(j<9)))
#print(j)

#part k
k=np.random.random(10)
k=np.sort(k)
#print(k)

#part l
A = np.random.randint(0,2,5)
B=np.random.randint(0,2,5)
equal=np.equal(A, B)
#print(equal)

#part m
m=np.arange(10, dtype=np.int32)
#print(m.dtype)
m=np.ndarray.astype(m, float)
#print(m.dtype)

#part n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
#print(D)