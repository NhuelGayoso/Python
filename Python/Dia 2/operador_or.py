print('*** Operador Logico OR ***')
condicion1 = False
condicion2 = False

# Aplicamo el operador or
resultado = condicion1 or condicion2
# El operador and si cualquiera de sus operadores
# es falso, todas las ecpresiones son falso
print(f"Resultado {condicion1} and {condicion2}: {resultado}")

# Supongamos que sergio quiere asistir al juego de su hijo
vacaciones = False
dia_descanso = False
if vacaciones or dia_descanso:
    print('Sergio puede asistir al juego de mateo')
else:
    print('Sergio esta trabajando, no puede ir al juego de mateo')
