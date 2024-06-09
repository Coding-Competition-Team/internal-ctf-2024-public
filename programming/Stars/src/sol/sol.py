from pwn import *
from subprocess import Popen, PIPE, STDOUT

r = remote("localhost", 7017)

for _ in range(100):
    print("Starting ...")
    start = r.recvuntil(b":\n")
    print(start)
    
    raw = b''
    while r.can_recv():
        raw += r.recvline()

    proc = Popen("./sol", stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    ans = proc.communicate(input=raw)[0].decode()
    print(ans)
    
    r.sendline(ans)
    
endmsg = r.recv().splitlines()
for i in endmsg:
    print(i)
r.close()