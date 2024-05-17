clc;
clear all;
close all;
fil = fopen('sinwave_oct.txt','r');
A = fscanf(fil,'%f')
fclose(fil);

f=10;
x=sin(2*pi*f*A);

plot(A,x)
