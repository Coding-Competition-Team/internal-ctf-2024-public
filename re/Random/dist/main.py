import random
import time

with open("flag.txt", "rb") as f:
    flag = f.read()

random.seed(int(time.time()))

def encrypt(plaintext):
    ciphertext = [a ^ random.randint(0, 126) for a in plaintext]

    random.shuffle(ciphertext)

    return bytearray(ciphertext).hex()

encrypted = encrypt(flag)
print(encrypted)

# output: 634833031027625221492253483233676d246b2b01574072305f16353b7474