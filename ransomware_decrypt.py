# ransomware_decrypt.py
import os
import zipfile

# Nombre del archivo ZIP predefinido
ZIP_FILENAME = "archivos_cifrados.zip"

# Solicitar la contraseña para desencriptar
user_password = input("Ingresa la contraseña para desencriptar los archivos: ")

def decrypt_files_from_zip(zip_filename, output_folder, password):
    """Desencripta los archivos en el archivo ZIP y los guarda en una carpeta."""
    with zipfile.ZipFile(zip_filename, "r") as zipf:
        # Verificar si el archivo "password_marker.txt" coincide con la contraseña proporcionada
        stored_password = zipf.read("password_marker.txt").decode()
        if stored_password != password:
            print("Error: La contraseña proporcionada no es correcta.")
            return

        # Verificar si el directorio de salida existe, si no, crearlo
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for encrypted_file in zipf.namelist():
            if encrypted_file == "password_marker.txt":
                continue  # Ignorar el archivo de marcador de contraseña

            encrypted_data = zipf.read(encrypted_file)

            # Guarda el archivo descifrado en la carpeta de salida
            original_file = os.path.splitext(encrypted_file)[0]
            output_path = os.path.join(output_folder, original_file)
            with open(output_path, "wb") as f:
                f.write(encrypted_data)

    # Borra el archivo ZIP una vez desencriptado
    os.remove(zip_filename)

if __name__ == "__main__":
    # Verificar la contraseña antes de solicitar la carpeta de salida
    with zipfile.ZipFile(ZIP_FILENAME, "r") as zipf:
        stored_password = zipf.read("password_marker.txt").decode()
        if stored_password != user_password:
            print("Error: La contraseña proporcionada no es correcta.")
            exit(1)

    # Solicitar la carpeta de salida solo si la contraseña es correcta
    output_folder = input("Ingresa la dirección de la carpeta donde se colocaran los archivos restaurados: ")
    decrypt_files_from_zip(ZIP_FILENAME, output_folder, user_password)
