import numpy as np

#for loadtxt data from csv file by numpy
'''
data=np.loadtxt("/home/pvtrmrt/data2.csv",delimiter=",")
print(data)
'''
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
fil=open("sinwave_numpy.txt","w")
np.savetxt(fil,x)
fil.close()
fil=open("sinwave_numpy.txt","r")
data=np.loadtxt(fil)
print(data)
fil.close()
