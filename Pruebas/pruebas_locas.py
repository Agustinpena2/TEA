try:

    archivo = input("Ingrese el nombre del archivo: ")
    f = open(archivo, "r")
    for linea in f:
    print(linea.upper())

    print("Este programa es para estimar la cantidad de metros cubicos de precipitacion de una area determinada")
    area = input("El area de interes (metros cuadrados) es: ")
    precipitacion = input("La precipitacion actual (mm) es de: ")
    Total = float(area)*(float(precipitacion)*0.001)
    print (Total)
except:
    print("Error, revisar los datos")
