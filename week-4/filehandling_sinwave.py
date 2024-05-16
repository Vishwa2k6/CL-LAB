import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)

#for write data
fil=open("sinwave.txt","w")
fil.write(str(x))
fil.close()

#for read data
fil=open("sinwave.txt","r")
z=fil.read()
print(z)
fil.close()

#for write data binary
fil=open("sinwave_bin.txt","wb")   #takes less storage in binary format
fil.write(x)   #no need to use str
fil.close()
#for read data

fil=open("sinwave_bin.txt","rb")
z=fil.read()
print(z)
fil.close()
