# Ransomware Simulation

This project provides a simple demonstration of file encryption and decryption using Python. Two scripts are included: one for encrypting files and storing them in a ZIP archive, and one for decrypting them. The process uses a password that the user provides and verifies before allowing decryption.

## Features

- **Encryption**: Encrypts files within a specified directory and stores them in a ZIP archive.
- **Decryption**: Decrypts files from the ZIP archive using a password marker for verification.
- **Password Verification**: Ensures files are decrypted only if the correct password is provided.

## Prerequisites

- Python 3.x
- Install `zipfile` (typically included with Python)

## Usage

### Encryption

1. **Setup**: Ensure you have Python 3 installed.
2. **Encrypt Files**:
   - Place the files you want to encrypt into a folder.
   - Run the `ransomware_encrypt.py` script.
   - Provide the folder's path and a password when prompted.
   - The script will generate a ZIP file called `archivos_cifrados.zip`.

### Decryption

1. **Setup**: Make sure you have Python 3 installed.
2. **Decrypt Files**:
   - Run the `ransomware_decrypt.py` script.
   - Enter the password used during encryption.
   - Provide the output folder where the decrypted files should be saved.
   - If the password matches the marker inside `archivos_cifrados.zip`, the files will be extracted and saved to the specified output folder.

## Important Notes

- **Security**: This project is for educational purposes only. It is a simple demonstration and should not be used for protecting sensitive information.
- **Password Storage**: The password is stored within the ZIP archive for validation purposes only.

## Members

- **Member 1:** Hector Gutierrez
- **Member 2:** Camila Rodriguez

## License

This project is provided for educational purposes and is not intended for malicious activities.
