my_name = "jose"

print(my_name)

age = 32
print(age)

age = 39
print(age)

# Tipado dinámico: el tipo de dato de una variable puede cambiar en tiempo de ejecución

print(type(age))

age = "39"
print(type(age))

## Tipado fuerte: Python no realiza conversiones de tipo de datos automáticamente

# print(2 + "3") # Error

age = int(age)

# f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age-3} años")

# No recomendada forma de asignar variables
name, age, city = "jose", 32, "Bogotá"

# Convensiones de tipos de datos
mi_nombre_de_variable = "ok"  #sanke_case

miNombreDeVariable = "no"  #camelCase
miNombreDeVariable = "ok"  #PascalCase

# Constantes (realmente si se puede cambiar el valor de una constante, es solo una convención)
MI_CONSTANTE = 10

# Comentarios del tipo de datos de la variable

is_user_admin: bool = True

# is_user_admin = 10 # Error

print(is_user_admin)



