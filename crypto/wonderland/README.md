# Wonderland

Author: I-En

> Wonderland is a wondrous place with wonderful wonders.  
> One of these wonders is wondencrypt, a patented encryption scheme that produces wonderful ciphertexts.  
> I wonder how they do it? I hear that the secret of this encryption is the flag of Wonderland...  

**Difficulty: Hard**

## Solution

We can exploit the wondecrypt method by rearranging our ciphertext.  
Since ECB is used to encrypt, we can move around blocks freely and decryption will still be the same. All we need to do is align the xor of the flag how we want.  

We want to put the encrypted flag first so when it removes the back with `pt[:-len(flag)]`, our flag still remains. To do this, we need to make sure the initial part of the flag xors with ciphertext of the ECB encrypted flag.  
All we need to do is find a multiple between 16 and 38 (size of flag) so we can use that many blocks before the flag, allowing the previously mentioned alignment. We use 19 blocks.  
After this, we need to create a new ct to decrypt, putting the flag in front, then using the 3rd to 6th block of our ciphertext, which continues to align for the xor.  
To prevent padding error, we send a padding block after the 5th block.  
After decryption, the server will remove the extra 3 blocks we sent, leaving the flag which is at the front.  