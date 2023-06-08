# en este codigo implementamos un proceso de cifrado y descifrado de archivos utilizando la biblioteca de criptografia "cryptography"
from cryptography.fernet import Fernet
import time


inicioE2 = time.time()
#Etapa 2: Generar y/o imprimir la(las) claves de cifrado
#Escribir y guardar clave

#genera_clave genera una nueva clave de cifrado utilizando la clase fernet 
def genera_clave():
    
    clave = Fernet.generate_key()

    with open("clave.key","wb") as archivo_clave: # la clave se guarda en un archivo llamado clave.key
        archivo_clave.write(clave)
    with  open('clave.key','r') as clave_lectura:
        print("La clave generada es: ")
        print(clave_lectura.read())

#cargar clave
def cargar_clave():
    return open("clave.key","rb").read()

#generar clave
genera_clave()
#cargar clave
clave = cargar_clave()
finE2 = time.time()


inicioE1 = time.time()

#Etapa 1: Leer el archivo
# abre y lee el contenido del archivo .txt utilizando el modo de lectura del texto rt
nom_archivo= "10 palabras.txt"

def leerArchivo():
    stream = open("10 palabras.txt", "rt", encoding="utf-8")
    print(stream.read())
leerArchivo()
finE1 = time.time()


inicioE3 = time.time()

#Etapa 3: Cifrar e imprimir el texto cifrado.
#Encriptar archivo

# la funcion encriptar(nom_archivo,clave) toma el nombre del aarchivo y la clave de cifrado como argumentos

def encriptar(nom_archivo, clave):
    f = Fernet(clave) # se crea el objeto fernet con la clave proporcionada 
    with open(nom_archivo, "rb") as file: # el archivo se abre en modo de lectura binaria rb y se lee el contenido 

        # el contenido del archivo se cifra utilizando la clave y se guarda en la misma ubicacion del archivo original
        # se lee y se imprime el contenido del archivo cifrado de la consola
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo,"wb") as file:
        file.write(encrypted_data)
    with  open(nom_archivo,'rb') as archivo_lectura:
        print("El archivo cifrado es: ")
        print(archivo_lectura.read())

encriptar(nom_archivo, clave)
finE3 = time.time()
       


#DESCENCRIPTAR
inicioE4 = time.time()
#Etapa 4: Descifrar e imprimir el texto claro.
#Desencriptar archivo

# la funcion desencriptar(nom_archivo, clave) toma el nombre del archivo y la clave de cifrado como argumentos 
def desencriptar(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        
         # el contenido del archivo se cifra utilizando la clave y se guarda en la misma ubicacion del archivo original
        # se lee y se imprime el contenido del archivo cifrado de la consola
        encrypted_data = file.read()
    desencrypted_data = f.decrypt(encrypted_data)
    with open(nom_archivo,"wb") as file:
        file.write(desencrypted_data)

#desencriptar e imprimir
desencriptar(nom_archivo, clave)
with  open(nom_archivo,'rt', encoding="utf-8") as archivo_lectura2:
        print("El archivo descifrado es: ")
        print(archivo_lectura2.read())
finE4 = time.time()

# finalmente se calcula el tiempo de ejecucion de cada etapa utilizando la funcion time.time() 
# los resultados se imprimen en la consola 

print("-----------------------")
print("Tiempo ejecución E1: ")
print(finE1-inicioE1)
print("-----------------------")
print("Tiempo ejecución E2: ")
print(finE2-inicioE2)
print("-----------------------")
print("Tiempo ejecución E3: ")
print(finE3-inicioE3) 
print("-----------------------")
print("Tiempo ejecución E4: ")
print(finE4-inicioE4)
print("-----------------------")