clc;
clear all;
close all;
x=0:0.01:1;
fil = fopen('sine.txt','w');
fprintf(fil,'%f\n',x);
fclose(fil);
