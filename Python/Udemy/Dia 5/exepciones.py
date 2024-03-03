print('*** Manejo de Excepciones ***')
try:
    # print(mi_variable)
    # 10/0
    x = int(input('Dame un de x: '))
    if x == 0:
        # Nos perminte arrojar una excepcion
        raise Exception('Error de la variable es 0')
except Exception as e:
    print(f'Ocurrio un error: {e}')
else:
    print('El valor de la variable x es distinto de 0')
finally:
    print(f'Valor de x validado {x}')
