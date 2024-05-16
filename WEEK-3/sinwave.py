import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,10,0.01)
f=5
x=np.sin(2*np.pi*f*t)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine wave')
plt.show()
