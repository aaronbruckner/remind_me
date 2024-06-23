#!/usr/bin/env python
import sys
from remindme import crypto
from scripts.encrypt import ENCRYPT_OUTPUT_PATH

DECRYPT_OUTPUT_PATH = "resources/raw_data_decrypted.yaml"

def encrypt_raw_data_file(password: str):
    with open(ENCRYPT_OUTPUT_PATH, "rb") as file:
        input_data = file.read()
    
    with open(DECRYPT_OUTPUT_PATH, 'wb') as file:
        # Write bytes to the file
        file.write(crypto.decrypt(data=input_data, password=password))

if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(f"Decrypting\n\tinput: {ENCRYPT_OUTPUT_PATH}\n\toutput: {DECRYPT_OUTPUT_PATH}")
    encrypt_raw_data_file(sys.argv[1])
    print("Done!")