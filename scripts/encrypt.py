#!/usr/bin/env python
import sys
from remindme import crypto

# Takes local uncommitted data file and encrypts it.

INPUT_PATH = "resources/raw_data.yaml"
ENCRYPT_OUTPUT_PATH = "resources/data.enc"

def encrypt_raw_data_file(password: str):
    with open(INPUT_PATH, "rb") as file:
        input_data = file.read()
    
    with open(ENCRYPT_OUTPUT_PATH, 'wb') as file:
        # Write bytes to the file
        file.write(crypto.encrypt(data=input_data, password=password))

if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(f"Encrypting\n\tinput: {INPUT_PATH}\n\toutput: {ENCRYPT_OUTPUT_PATH}")
    encrypt_raw_data_file(sys.argv[1])
    print("Done!")