import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin_dict={'s1':[1,5],'s2':[6,10],'s3':[11,15]}

print("choose: {'s1':[1,5],'s2':[6,10],'s3':[11,15]}") 

n=input("Enter sinusoidal key to generate:")

if sin_dict[n]:
    x=sin_dict[n][0]*np.sin(2*np.pi*sin_dict[n][1]*t) #first sin_dict[k][0] is amplitude
    plt.plot(t,x)
    plt.show()
