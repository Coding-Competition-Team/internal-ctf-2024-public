from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

with open('flag.txt', 'rb') as f:
    flag = f.read().strip() #38 bytes

key = os.urandom(16)

class Wonderland:
    def __init__(self):
        self.key = os.urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)
    
    # patented wonder encryption
    def wondencrypt(self, pt):
        padded = pad(pt + flag, 16)
        ct = self.cipher.encrypt(padded)
        xor = flag * ((len(ct) // len(flag)) + 1)
        ct = bytes([a^b for a, b in zip(ct, xor)])
        return ct.hex()
    
    # decrypts wonder ciphertext
    def wondecrypt(self, ct):
        xor = flag * ((len(ct) // len(flag)) + 1)
        pt = bytes([a^b for a, b in zip(ct, xor)])
        pt = self.cipher.decrypt(pt)
        pt = unpad(pt, 16)
        pt = pt[:-len(flag)]
        return pt.hex()


def options():
    print("Options:")
    print("1. WondEncrypt")
    print("2. WonDecrypt")


if __name__=="__main__":
    print("I wonder if you can get the flag?\n")
    wonder = Wonderland()
    
    while True:
        options()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            pt = bytes.fromhex(input("Enter your wonderful plaintext: "))
            ct = wonder.wondencrypt(pt)
            print(f"Your wonderful ciphertext is: {ct}\n")
        
        elif choice == 2:
            ct = bytes.fromhex(input("Enter your wonderful ciphertext: "))
            pt = wonder.wondecrypt(ct)
            print(f"Your wonderful plaintext is: {pt}\n")
        
        else:
            print("Have a wonderful day.")
            exit(0)