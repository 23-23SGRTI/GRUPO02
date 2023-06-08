import time #contiene una serie de funciones relacionadas con la medición del tiempo

# provee de primitivas criptográficas (algoritmos criptográficos de bajo nivel)
from crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

inicioE2 = time.time()
# Etapa 2: Generar y/o imprimir la(s) claves de cifrado

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,   #Se puede cambiar a 1024
    backend=default_backend()
)
public_key = private_key.public_key()

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Crear archivos de las claves pública y privada

with open("private.pem", "wb") as file_out:
    file_out.write(private_pem)

with open("receiver.pem", "wb") as file_out:
    file_out.write(public_pem)

# Salida de pantalla

print(public_pem.decode())
print(private_pem.decode())
finE2 = time.time()


inicioE1 = time.time()
# Etapa 1: Leer el archivo
with open("texto1.txt", "rb") as file_in:#SE CAMBIA EL ARCHIVO AQUI
    data = file_in.read()
    lectura = data.decode("utf-8")
print("-------------------MENSAJE-----------------------")
print("\nLectura del archivo")
print(lectura)
print("-----------------------------------------")
finE1 = time.time()


inicioE3 = time.time()
# Etapa 3: Cifrar e imprimir el texto cifrado
recipient_public_key = serialization.load_pem_public_key( # se convierte en un objeto PublicKey utilizando la función serialization.load_pem_public_key()
    open("receiver.pem", "rb").read(),
    backend=default_backend()
)
session_key = get_random_bytes(16) #se genera una clave de 16 bytes

ciphertext = recipient_public_key.encrypt( #Se cifra la clave de sesión utilizando la clave pública del receptor
    session_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

cipher = Cipher( #para cifrar los datos
    algorithms.AES(session_key),
    modes.CTR(get_random_bytes(16)),
    backend=default_backend()
)
encryptor = cipher.encryptor() #el texto cifrado se escribe en un archivo llamado
encrypted_data = encryptor.update(data) + encryptor.finalize()

# Escribir el texto cifrado en un archivo
with open("encrypted_data.bin", "wb") as file_out:
    file_out.write(ciphertext)
    file_out.write(encrypted_data)

# Leer el archivo binario y luego imprimir
with open("encrypted_data.bin", "rb") as file_in:
    variable = file_in.read()
    print("Información cifrada")
    print(variable)
finE3 = time.time()


inicioE4 = time.time()
# Etapa 4: Descifrar e imprimir el texto claro
private_key = serialization.load_pem_private_key( #Se carga la clave privada del receptor desde el archivo
    open("private.pem", "rb").read(),
    password=None,
    backend=default_backend()
)

ciphertext = private_key.decrypt( #utiliza la clave privada para descifrar la clave de sesión cifrada.
    variable[:private_key.key_size // 8],
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

cipher = Cipher(
    algorithms.AES(session_key),
    modes.CTR(get_random_bytes(16)),
    backend=default_backend()
)

#esta sección del código carga la clave
#privada del receptor, descifra la clave
#de sesión utilizando la clave privada

print("\nInformación descifrada")
finE4 = time.time()
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