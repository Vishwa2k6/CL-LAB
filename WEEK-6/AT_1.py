from matplotlib import pyplot as plt
import numpy as np
x = []
y = []
lenx = int(input("Enter length of x: "))
leny = int(input("Enter length of y: "))
print("Enter elements into x:")
for i in range(lenx):
    a = int(input("Enter: "))
    x.append(a)  
print("Enter elements into y:")
for i in range(leny):
    a = int(input("Enter: "))
    y.append(a)
z = []
for k in range(leny - 1):
    s = 0
    for n in range(lenx):
        if n + k < lenx:
            s += x[n] * y[n + k]
    z.append(s)
plt.plot(z)
plt.xlabel('Lag')
plt.ylabel('Cross-correlation')
plt.title('Cross-correlation between x and y')
plt.show()
