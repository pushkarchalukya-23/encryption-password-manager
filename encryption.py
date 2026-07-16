from config import ENCRYPTION_KEY,ENCRYPTION_STRING

def encrypt(password):
    encrypted = ""
    for i in password:
        encrypted += ENCRYPTION_STRING[ENCRYPTION_STRING.find(i) - ENCRYPTION_KEY]
    return encrypted

# A Slow Hashing == (bcrypt , scrypt , argon2) using function which delays guesses/sec 
# B hashing + salting  == a good way
# C hashing  == (MD5 , SHA-1 , SHA-2) one way function to hash a function ,, but beware of rainbow tables
# D encrypt  == just make two strings and get indexes matched

def decrypt(encrypted):
    decrypted = ""
    for i in encrypted:
        if (ENCRYPTION_STRING.find(i) + ENCRYPTION_KEY) > len(ENCRYPTION_STRING) - 1:
            decrypted += ENCRYPTION_STRING[ENCRYPTION_STRING.find(i) + ENCRYPTION_KEY - len(ENCRYPTION_STRING) ]
        else:
            decrypted += ENCRYPTION_STRING[ENCRYPTION_STRING.find(i) + ENCRYPTION_KEY]
    return decrypted
