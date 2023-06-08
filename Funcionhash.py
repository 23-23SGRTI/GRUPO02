
import hashlib  #proporciona una función de ayuda para el cifrado
import time #contiene una serie de funciones relacionadas con la medición del tiempo

print("------------------PALABRAS-----------------")

archivo = "texto1.txt" #CAMBIO DE TEXTO
inicioE1 = time.time()
#Etapa 1: Leer el archivo
def leerArchivo():
    stream = open(archivo, mode = "rt", encoding= 'utf-8') # Abrir archivo en modo de texto
    print(stream.read()) # Leer y muestra el contenido del archivo
leerArchivo()   # Llamar a la función para leer el archivo
finE1 = time.time()

inicio = time.time() 

print("")
print("VALOR HASH")
print("------------------------")

with open(archivo,"rb") as file: # Abrir archivo en modo de lectura de bytes
    bytes = file.read() # Leer el contenido del archivo en bytes
    genera_hash = hashlib.sha256(bytes).hexdigest() # Calcular el valor hash SHA-256 del contenido
    print(genera_hash) # Imprimir el valor hash

fin = time.time()

# ejecuta los tiempos
print("-----------------------")
print("Tiempo ejecución E1: ")
print(finE1-inicioE1)
print("-----------------------")
print("Tiempo transcurrido: ")
print(fin-inicio)