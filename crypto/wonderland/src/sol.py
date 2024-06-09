from pwn import *

'''
We can exploit the wondecrypt method by rearranging our ciphertext.
Since ECB is used to encrypt, we can move around blocks freely and decryption will still be the same. All we need to do is align the xor of the flag how we want.

We want to put the encrypted flag first so when it removes the back with pt[:-len(flag)], our flag still remains. To do this, we need to make sure the initial part of the flag xors with ciphertext of the ECB encrypted flag.
All we need to do is find a multiple between 16 and 38 (size of flag) so we can use that many blocks before the flag, allowing the previously mentioned alignment. We use 19 blocks.
After this, we need to create a new ct to decrypt, putting the flag in front, then using the 3rd to 6th block of our ciphertext, which continues to align for the xor.
To prevent padding error, we send a padding block after the 5th block.
After decryption, the server will remove the extra 3 blocks we sent, leaving the flag which is at the front.
'''

if __name__=="__main__":
    conn = remote("localhost", 4000)
    conn.recv()
    
    pt = "00"*(16*5) + "10"*16 + "00"*(16*13) # 19 blocks, with a padding block as the 6th block to prevent padding error
    conn.sendline(b"1")
    conn.recv()
    conn.sendline(pt.encode())
    conn.recvuntil(b"Your wonderful ciphertext is: ")
    ct = conn.recvline()[:-1].decode()
    conn.recv()
    
    newct = ct[-16*2*3:] + ct[16*2*3:16*2*6] # put the flag first
    conn.sendline(b"2")
    conn.recv()
    conn.sendline(newct.encode())
    ct = bytes.fromhex(newct)
    conn.recvuntil(b"Your wonderful plaintext is: ")
    flag = conn.recvline()[:-1].decode()
    conn.recv()
    conn.close()
    
    print(f"flag is: {bytes.fromhex(flag).decode()[:38]}")