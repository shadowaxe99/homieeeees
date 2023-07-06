```python
import os
from cryptography.fernet import Fernet

class SecurityPrivacy:
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """Encrypts the data"""
        cipher_text = self.cipher_suite.encrypt(data)
        return cipher_text

    def decrypt_data(self, cipher_text):
        """Decrypts the data"""
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text

    def secure_file(self, file_path):
        """Encrypts the file for secure storage"""
        with open(file_path, 'rb') as file:
            encrypted_data = self.encrypt_data(file.read())
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def retrieve_file(self, file_path):
        """Decrypts the file for use"""
        with open(file_path, 'rb') as file:
            decrypted_data = self.decrypt_data(file.read())
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
```