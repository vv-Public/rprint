import hashlib
import base64
import sys 


def generaate_hash_value():
    filename = "app.py"
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        
        # get the sha256 encoded hash value
        hvl = (sha256_hash.hexdigest().encode())
        # chop the string down from 64 to 32 using md5 to hash the hash
        hvl =hashlib.md5(hvl).hexdigest()
        return hvl


hv= generaate_hash_value()

print (hv)
