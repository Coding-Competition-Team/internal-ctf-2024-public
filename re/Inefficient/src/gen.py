from Crypto.Util.number import *
import random

with open("flag.txt", "rb") as f:
    flag = f.read()

listP = []
listQ = []
listE = []
keys = []
magicNums = []

for i in range(len(flag)):
    listP.append(getPrime((i + 10) * 7))
    listQ.append(getPrime((i + 10) * 7))
    listE.append(getPrime(i + 4))
    keys.append(random.randint(0,256))
    phi = (listP[i] - 1) * (listQ[i] - 1)
    d = pow(listE[i], -1, phi)
    magicNums.append(pow(keys[i], d, listP[i] * listQ[i]))

encrypted = [flag[i] ^ keys[i] for i in range(len(flag))]
print(f"{listP=}")
print(f"{listQ=}")
print(f"{listE=}")
print(f"{keys=}")
print(f"{magicNums=}")
print(f"{encrypted=}")
