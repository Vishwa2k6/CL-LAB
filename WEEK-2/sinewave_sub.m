clear all;
close all;
clc;
f1=5;
f2=10;
t=0:0.01:1;
x=sin(2*pi*f1*t);
y=sin(2*pi*f2*t);

z=y-x;
plot(t,z);
