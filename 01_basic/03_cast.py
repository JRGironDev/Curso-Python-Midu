# Conversión de tipos de datos

print(type(int("100")))

print(2 + int("100"))

print("100" + str(10))

print(float("100.5232"))
print(int(100.5232))
print(int(2.9))

print(bool(3)) # True
print(bool(0)) # False
print(bool(1)) # True

print(bool("")) # False
print(bool(" ")) # True
print(bool("False")) # True
print(bool("True")) # True

# Round
print(round(100.5232))