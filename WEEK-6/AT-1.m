clc;
clear all;
close all;
x=[];
lenx=input("Enter length of array:");
y=0;
for i=1:lenx
  f=input("Enter x[n]:")
  x=[x,f];
end
leny=input("Enter length of y[k]:")
k=1:0.01:leny;

for i=1:lenx
  y+=x(i)*cos(2*pi*i*k);
end
plot(y);
