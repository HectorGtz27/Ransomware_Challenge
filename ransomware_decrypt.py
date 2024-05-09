# ransomware_decrypt.py
import os
import zipfile
from cryptography.fernet import Fernet

def load_key():
    """Carga la clave desde el archivo."""
    return open("encryption.key", "rb").read()

def decrypt_files_from_zip(zip_filename, output_folder):
    """Desencripta los archivos en el archivo ZIP y los guarda en una carpeta."""
    key = load_key()
    cipher = Fernet(key)

    with zipfile.ZipFile(zip_filename, "r") as zipf:
        for encrypted_file in zipf.namelist():
            encrypted_data = zipf.read(encrypted_file)
            decrypted_data = cipher.decrypt(encrypted_data)

            # Guarda el archivo desencriptado en la carpeta de salida
            original_file = os.path.splitext(encrypted_file)[0]
            output_path = os.path.join(output_folder, original_file)
            with open(output_path, "wb") as f:
                f.write(decrypted_data)

    # Borra el archivo ZIP una vez desencriptado
    os.remove(zip_filename)

if __name__ == "__main__":
    zip_filename = input("Ingresa el nombre del archivo ZIP a desencriptar (ejemplo: archivos_cifrados.zip): ")
    output_folder = input("Ingresa la dirección de la carpeta para restaurar los archivos: ")
    decrypt_files_from_zip(zip_filename, output_folder)
