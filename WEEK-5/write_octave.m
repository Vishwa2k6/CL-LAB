clc;
close all;
clear all;
str = '78°C 72°C 64°C 66°C 49°C';
fil = fopen('temp.dat','w');
fprintf(fil,'%s',str);
fclose(fil);
