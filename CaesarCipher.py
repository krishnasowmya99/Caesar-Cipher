def encrypt(plaintext, key):
    """
    Encrypts plaintext using Caesar Cipher with the given key.
    Returns the ciphertext.
    """
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            shifted = ord(letter) + key
            if letter.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            elif letter.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += letter
    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Caesar Cipher with the given key.
    Returns the plaintext.
    """
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            shifted = ord(letter) - key
            if letter.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            elif letter.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += letter
    return plaintext


plaintext = "Hello, Sowmya Kothwalgudem!"
key = 3
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_plaintext = decrypt(ciphertext, key)
print(f"Decrypted plaintext: {decrypted_plaintext}")
