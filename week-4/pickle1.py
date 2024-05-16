#pickle module is used to r/w from binary file
#pickle.dump(DATA,FILE_handle)-> write datastructure
#pickle.load(file_handle)->read

import numpy as np
import pickle
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
#write data into file by pickle.dump()
fil=open("pickle1.txt","wb")
pickle.dump(x,fil)
fil.close()

#read data from file by pickle.load()
fil=open("pickle1.txt","rb")
n=pickle.load(fil)
print(n)
fil.close()
