# Reglas definir el nombre de variables

# 1. Comenzar con la letra o guion bajo (_)
_mi_variable = 30

# 2. Puede continuar con letras, numeros o guion bajo
# 3mi_variable2 = 40 # esto arroja un error
mi_variable2 = 40

# 3. Sensible a mayusculas y minusculas
# print(Mi_variable2) arroja error
print(mi_variable2)

# 4.No se pueden usar palabras reservadas (keyword)
# class, if, for, while
# class = 50 error
klass = 50
print(klass)

# Buenas practicas en Python
nombre_usuario = 'Nahuel'  # Notacion snake case
nombreUsuario = 'Norberto'  # Notacion camelcase (no se recomienda en python)
NombreUsuario = 'Rocio'  # Notacion pascal (no se recomienda en python)
