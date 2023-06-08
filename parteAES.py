from cryptography.fernet import Fernet
import time


inicioE2 = time.time()
#Etapa 2: Generar y/o imprimir la(las) claves de cifrado
#Escribir y guardar clave

# la funcion genera_clave() genera una nueva clave de cifrado utilizando la clase fernet 
def genera_clave():
# la clave se guarda en un archivo llamado clave.key utilizando el modo de escritura binaria wb 
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)
    with  open('clave.key','r') as clave_lectura:
        print("La clave generada es: ")
        print(clave_lectura.read())

#cargar clave
# la funcion cargar_clave() lee el contenido del archivo clave.key en modo de lectura binaria rb y devuelve el contenido de la clave
def cargar_clave():
    return open("clave.key","rb").read()

#generar clave
# la funcion genera_clave para generar una nueva clase y se guarda en la variable clave 
genera_clave()
#cargar clave
clave = cargar_clave()
# luego se calcula el tiempo de inicio de esta etapa utilizando el time.time() y se guarda en la varibale inicioE2
finE2 = time.time()


inicioE1 = time.time()

#Etapa 1: Leer el archivo
# se especifica el nombre del archivo a leer como .txt
nom_archivo= "texto1.txt"

# la funcion leerArchivo() abre el archivo en modo lectura de texto rt con codificacion UFT-8 y lee su contenido
def leerArchivo():
    stream = open("texto1.txt", "rt", encoding="utf-8")
# se imprime el contenido del archivo en la consola
    print(stream.read())
leerArchivo()
# se calcula el tiempo de finalizacion de esta etapa utilizando time.time() y se guarda en la varibale finE1
finE1 = time.time()


inicioE3 = time.time()
#Etapa 3: Cifrar e imprimir el texto cifrado.
#Encriptar archivo

#la funcion encriptar(nom_archivo, clave) toma el nombre del archivo y la clave de cifrado como argumentos
def encriptar(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo,"wb") as file:
        file.write(encrypted_data)
    with  open(nom_archivo,'rb') as archivo_lectura:
        print("El archivo cifrado es: ")
        print(archivo_lectura.read())

# la funcion encriptar(nom_archivo, clave) para cifrae el archivo utilizando la clave generada en la etapa anterior
encriptar(nom_archivo, clave)
# se calcula el tiempo de finalizacion de esta etapa utilizando time.time() y se guarda en la variable
finE3 = time.time()



