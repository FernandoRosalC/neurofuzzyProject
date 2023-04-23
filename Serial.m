clear all;
clc;

s = serial('COM4', 'BaudRate', 9600);
fclose(instrfind);
fopen(s);

while true
    % Leer una línea completa desde la conexión serial
    line = fgetl(s);

    flushinput(s);

    % Convertir la cadena en valores separados por comas
    values = sscanf(line, '%f,%f,%d');

    % Asignar los valores a variables individuales
    temp_actual = values(1);
    temp_requerida = values(2);
    contador_personas = values(3);

    % Hacer algo con los valores
    disp(['Temperatura actual: ', num2str(temp_actual)]);
    disp(['Temperatura requerida: ', num2str(temp_requerida)]);
    disp(['Contador de personas: ', num2str(contador_personas)]);
end

fclose(s);






