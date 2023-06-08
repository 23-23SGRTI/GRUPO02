import time

def generar_clave():
    # Genera una clave aleatoria de sustitución
    letras_originales = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    letras_mezcladas = "QZMBOÑFUAPHCLKIWVGJNYEXTRSD"
    clave = {}
    for i in range(len(letras_originales)):
        clave[letras_originales[i]] = letras_mezcladas[i]
    return clave
inicioE1 = time.time()
def cifrar(texto, clave):
    texto_cifrado = ''
    for caracter in texto:
        if caracter.isalpha() and caracter.upper() in clave:
            # Sustituye el caracter según la clave de cifrado
            caracter_cifrado = clave[caracter.upper()]
            # Mantiene la capitalización original
            if caracter.islower():
                caracter_cifrado = caracter_cifrado.lower()
            # Construye el texto cifrado
            texto_cifrado += caracter_cifrado
        else:
            # Conserva los caracteres no alfabéticos
            texto_cifrado += caracter
    return texto_cifrado
finE1 = time.time()

inicioE2 = time.time()
def descifrar(texto_cifrado, clave):
    texto_descifrado = ''
    for caracter in texto_cifrado:
        if caracter.isalpha() and caracter.upper() in clave.values():
            # Busca el caracter original según la clave de descifrado
            for key, value in clave.items():
                if caracter.upper() == value:
                    caracter_descifrado = key
                    break
            # Mantiene la capitalización original
            if caracter.islower():
                caracter_descifrado = caracter_descifrado.lower()
            # Construye el texto descifrado
            texto_descifrado += caracter_descifrado
        else:
            # Conserva los caracteres no alfabéticos
            texto_descifrado += caracter
    return texto_descifrado

finE2 = time.time()

inicioE3 = time.time()
# Archivo de texto a cifrar
archivo_original = '1000000 palabras.txt'

# Leer el archivo de texto

with open(archivo_original, 'rb') as file:
    contenido_binario = file.read()
    texto_original = contenido_binario.decode('utf-8')

# Generar una clave de cifrado
clave = generar_clave()

# Cifrar el texto
start_time = time.time()
texto_cifrado = cifrar(texto_original, clave)
end_time = time.time()

# Imprimir la clave de cifrado
print("Clave de cifrado:", clave)
finE3 = time.time()
# Imprimir el texto cifrado
#print("Texto cifrado:")
#print(texto_cifrado)
inicioE4 = time.time()
# Escribir el texto cifrado en un nuevo archivo
archivo_cifrado = '1000000 palabras_cifrado.txt'
with open(archivo_cifrado, 'w') as file:
    file.write(texto_cifrado)

# Descifrar el texto cifrado
start_time = time.time()
texto_descifrado = descifrar(texto_cifrado, clave)
end_time = time.time()

# Escribir el texto descifrado en un nuevo archivo
archivo_descifrado = '1000000 palabras_descifrado.txt'
with open(archivo_descifrado, 'w') as file:
    file.write(texto_descifrado)
finE4 = time.time()
# Calcular el tiempo de descifrado en milisegundos

#tiempos de ejecución
print("-----------------------")
print("Tiempo ejecución E1: ")
print(finE1 - inicioE1)
print("-----------------------")
print("Tiempo ejecución E2: ")
print(finE2 - inicioE2)
print("-----------------------")
print("Tiempo ejecución E3: ")
print(finE3 - inicioE3)
print("-----------------------")
print("Tiempo ejecución E4: ")
print(finE4 - inicioE4)
print("-----------------------")