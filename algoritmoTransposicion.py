import time


inicioE1 = time.time()
#Etapa 1: Leer el archivo
def leerArchivo():
    stream = open("10 palabras.txt", mode = "rt", encoding= 'utf-8')
    print(stream.read())
leerArchivo()
finE1 = time.time()

inicioE3 = time.time()
#Etapa 3: Cifrar e imprimir el texto cifrado.
def cifrado():
    filename = '10 palabras.txt'
    with open(filename, encoding= 'utf-8') as f_obj:
        lines = f_obj.read()

    auxiliar = ""
    i = len(str(lines)) - 1
    while i >= 0:
        auxiliar = auxiliar + (lines[i])
        i = i - 1
    archivo = open('encriptado.txt', mode = "w", encoding= 'utf-8')
    archivo.write(auxiliar)
    print("\nArchivo creado con exito!!!!")
    print(auxiliar)

cifrado()   
finE3 = time.time()

inicioE4 = time.time()
#Etapa 4: Descifrar e imprimir el texto claro.
def descifrado():
    
    filename = 'encriptado.txt'
    with open(filename , encoding= 'utf-8') as f_obj:
        lines = f_obj.read()

    auxiliar = ""
    i = len(str(lines)) - 1
    while i >= 0:
        auxiliar = auxiliar + (lines[i])
        i = i - 1
    archivo = open('desencriptado.txt', mode = "w", encoding= 'utf-8')
    archivo.write(auxiliar)
    print("\nArchivo creado con exito!!!!")
    print(auxiliar)
    
descifrado()
finE4 = time.time()


print("-----------------------")
print("Tiempo ejecución E1: ")
print(finE1-inicioE1)
print("-----------------------")
print("Tiempo ejecución E2: ")
print("No existe clave generada")
print("-----------------------")
print("Tiempo ejecución E3: ")
print(finE3-inicioE3) 
print("-----------------------")
print("Tiempo ejecución E4: ")
print(finE4-inicioE4)
print("-----------------------")

