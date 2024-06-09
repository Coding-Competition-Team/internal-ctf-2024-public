from Crypto.Util.number import getPrime, bytes_to_long
from gmpy2 import invert

message = b'ACSI{sm4ll_e5s_4re_pr3tty_d4ng3r0us_right?}'
e = 3
d = -1

while d == -1:
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    try:
        d = invert(e, phi)
    except ZeroDivisionError:
        pass
m = bytes_to_long(message)
c = pow(m, e, n)