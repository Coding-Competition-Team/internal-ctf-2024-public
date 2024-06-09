from pwn import *
from randcrack import RandCrack
from Crypto.Util.number import long_to_bytes, bytes_to_long

rc = RandCrack()

r = remote("localhost", "4001")

for i in range(624):
    response = r.recv().strip()
    r.send(b'1\n')
    response = r.recv().strip()
    r.send(b'hello\n')
    xored = int(r.recvline().strip().decode())
    rand = xored ^ bytes_to_long(b'hello')
    rc.submit(rand)

predicted = rc.predict_getrandbits(32)
response = r.recv().strip()
r.send(b'2\n')
response = r.recvline().strip().decode()
r.close()
flag = int(response) ^ predicted
print(long_to_bytes(flag))
