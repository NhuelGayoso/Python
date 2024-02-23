print('*** Operador Logico AND ***')
condicion1 = False
condicion2 = False

# Aplicamo el operador and
resultado = condicion1 and condicion2
# El operador and si cualquiera de sus operadores
# es falso, todas las ecpresiones son falso
print(f"Resultado {condicion1} and {condicion2}: {resultado}")

# Ejemplo if else con operador and
llueve = False
nublado = True

print(f'\n*** Revision del clima ***')
if llueve and nublado:
    print('LLevar paraguas e impermeable, llueve y esta nublado')
elif llueve:
    print('Llevar paraguas, va a llover')
elif nublado:
    print('Llevar impermeable, solo esta nublado')
else:
    print('Dejar paraguas e impermeable, disfruta el dia')
