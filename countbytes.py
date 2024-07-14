#Function to Count bytes
import sys
import os

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            print(f" {len(data)} {file_path}")
    except FileNotFoundError:
        print(f" File {file_path} not found.")