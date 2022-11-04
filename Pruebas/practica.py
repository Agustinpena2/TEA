archivo = input("Ingrese el nombre del archivo: ")
f = open(archivo)
contador = 0
for linea in f:
    if linea.startswith("Subject:"):
        contador = contador + 1
print("Hay", contador,"líneas de asunto (subject) en", archivo)