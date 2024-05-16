clc;
clear all;
fclose all;
t=0:0.01:1
f=5
x=sin(2*pi*f*t)
fil=fopen('octave.txt','wt')
fwrite(fil,t);
fclose(fil);
fil=open('octave.txt','rt')
x=fread(fil)
fclose(fil)
plot(t,x)
