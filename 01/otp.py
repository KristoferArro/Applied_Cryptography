#!/usr/bin/env python3
import os, sys       # do not use any other imports/libraries
# took 1.5 hours (please specify here how much time your solution required)

def bi(b):
    # b - bytes to encode as an integer
    i = 0
    for by in b:
        i = (i << 8) | by
    return i

def ib(i, length):
    # i - an integer to encode as bytes
    # length - specifies in how many bytes the integer should be encoded
    b = b''
    for _ in range(length):
        b = bytes([i & 0xff]) + b
        i = i >> 8
    return b

# Disclaimer: Comments were added for my own understanding, while developing
def encrypt(pfile, kfile, cfile):
    # Open p file and convert to int
    p = open(pfile, 'rb').read()
    p_to_int = bi(p)
    # Generate key and convert key to in
    key = os.urandom(len(p))
    k_to_int = bi(key)
    # use XOR p and key to get cyphered
    c_to_int = p_to_int ^ k_to_int

    # Save key to file
    key_file = open(kfile, 'wb')
    key_file.write(key)
    key_file.close()

    # Convertt to bytes and save to c file
    int_to_bytes = ib(c_to_int, len(p))
    cypher_text = open(cfile, 'wb')
    cypher_text.write(int_to_bytes)
    cypher_text.close()

def decrypt(cfile, kfile, pfile):
    # Reverse order of encrypt
    # Open c file and and convert to int
    cypher_text = open(cfile, 'rb').read()
    c_to_int = bi(cypher_text)

    # Open key file and convert to int
    key = open(kfile, 'rb').read()
    k_to_int = bi(key)

    # Decypher p and convert to bytes
    p_to_int = c_to_int ^ k_to_int
    p_text = ib(p_to_int, len(cypher_text))

    # Write the converted bytes to p file
    p = open(pfile, 'wb')
    p.write(p_text)
    p.close()

def usage():
    print("Usage:")
    print("encrypt <plaintext file> <output key file> <ciphertext output file>")
    print("decrypt <ciphertext file> <key file> <plaintext output file>")
    sys.exit(1)

if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt':
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()
