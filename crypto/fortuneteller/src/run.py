import random
from Crypto.Util.number import bytes_to_long

flag = "ACSI{i_c3n_pr3d1ct_th3_futu53!}aaaa"
print("""
    Welcome to my fortuneteller!
    Options:
    1. Encrypt a random sentence!
    2. Encrypt and output the flag!""")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        sentence = input("Enter a sentence: ")
        rand = random.getrandbits(32)
        sentence = bytes_to_long(sentence.encode())
        result = int(sentence) ^ rand
        print(result)
    elif choice == "2":
        flag = bytes_to_long(flag.encode())
        rand = random.getrandbits(32)
        result = int(flag) ^ rand
        print(flag)
        input("Input anything to exit")
        break
    else:
        print("Invalid choice! Please try again!")
