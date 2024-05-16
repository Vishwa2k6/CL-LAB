t = 0:0.01:1;
sin1 = containers.Map({'s1','s2','s3'}, {[1,5],[6,10],[11,15]});

disp('Choose: {''s1'':[1,5],''s2'':[6,10],''s3'':[11,15]}');
k = input('Enter sinusoidal key to generate:','s');

if isKey(sin1, k)
    x = sin1(k)(1) * sin(2 * pi * sin1(k)(2) * t);
    plot(t, x);
    xlabel('Time');
    ylabel('Amplitude');
    title(['Sinusoidal Signal: ' k]);
    grid on;
    legend('Signal');
else
    disp('Invalid key. Please choose a valid key from the dictionary.');
end
