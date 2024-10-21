import os
from appwrite_client import upload_chunk

def split_file(file_path, chunk_size=1024 * 1024):
    with open(file_path, 'rb') as f:
        chunk_index = 0
        while chunk := f.read(chunk_size):
            with open(f"{file_path}_part_{chunk_index}", 'wb') as chunk_file:
                chunk_file.write(chunk)
                upload_chunk(f"{file_path}_part_{chunk_index}")
            chunk_index += 1

def reassemble_file(chunks, output_file):
    with open(output_file, 'wb') as outfile:
        for chunk in chunks:
            with open(chunk, 'rb') as infile:
                outfile.write(infile.read())
