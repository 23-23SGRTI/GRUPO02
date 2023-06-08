from cryptography.fernet import Fernet
import time

# se especifica el nombre del archivo a descifrar como.txt
nom_archivo= "texto1.txt"

#cargar clave
# la funcion cargar_clave() lee el cotenido del archivo clave.key en modo de lectura binaria rb y devuelve contenido de la clave

def cargar_clave():
    return open("clave.key","rb").read()

# la funcion cargar_clave() para cargar la clave desde el archivo clave.key
#cargar clave
clave = cargar_clave()
# se calcula el tiempo de finalizacion de esta etapa utilizando time.time() y se guarda en la variable finE2
finE2 = time.time()

#DESCENCRIPTAR
inicioE4 = time.time()
#Etapa 4: Descifrar e imprimir el texto claro.
#Desencriptar archivo

# la funcion esencriptar(nom_archivo, clave) toma el nombre del archivo y clave de cifrado como argumentos 
def desencriptar(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        encrypted_data = file.read()
    desencrypted_data = f.decrypt(encrypted_data)
    with open(nom_archivo,"wb") as file:
        file.write(desencrypted_data)
#desencriptar e imprimir
desencriptar(nom_archivo, clave)
with  open(nom_archivo,'rt', encoding="utf-8") as archivo_lectura2:
        print("El archivo descifrado es: ")
        print(archivo_lectura2.read())
# se calcula el tiempo de finalizacion de esta etapa utilizando time.time() y se guarda en la variable finE4
finE4 = time.time()