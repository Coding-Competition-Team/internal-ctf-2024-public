from pwn import *
from subprocess import Popen, PIPE, STDOUT

r = remote("localhost", 7016)

for _ in range(100):
    print("Starting ...")
    start = r.recvuntil(b":\n")
    print(start)
    
    raw = b''
    while r.can_recv():
        raw += r.recvline()
    # raw = r.recv()
    
    # lines = raw[:-1].splitlines()
    # raw = raw.strip()
    
    # context.log_level = 'debug'
    # p = process("./sol")
    # p.sendline(raw)
    # p.sendline(lines[0])
    
    # for i in range(len(lines) - 1):
    #     p.sendline(lines[i+1])
        # if i % 2 == 1:
        #     ans = p.recv()
        #     # print(ans)
        #     r.sendline(ans[:-1])
    # ans = p.recv(timeout=5)
    proc = Popen("./sol", stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    ans = proc.communicate(input=raw)[0].decode()
    print(ans)
    
    # print(ans)
    # print(raw[:10])
    r.sendline(ans)

    # p.close()
    
endmsg = r.recv().splitlines()
for i in endmsg:
    print(i)
r.close()