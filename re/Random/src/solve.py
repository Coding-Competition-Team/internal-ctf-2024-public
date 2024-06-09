import random
from binascii import unhexlify
from datetime import datetime
import pytz
import numpy as np
# https://stackoverflow.com/questions/12165691/python-datetime-with-timezone-to-epoch

tz = pytz.timezone("Asia/Singapore")
sevenpm = tz.localize(datetime(2024, 5, 22, 19, 0, 0), is_dst=None)
finalTime = tz.localize(datetime(2024, 5, 22, 23, 59, 0), is_dst=None)

startTime = int((sevenpm - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds())
finalTime = int((finalTime - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds())

ciphertext = unhexlify("634833031027625221492253483233676d246b2b01574072305f16353b7474")

# https://stackoverflow.com/questions/26577517/inverse-of-random-shuffle
def shuffle_forward():
    order = list(range(len(ciphertext))); random.shuffle(order)
    return order

def shuffle_backward(l, order):
    l_out = [0] * len(l)
    for i, j in enumerate(order):
        l_out[j] = l[i]
    return l_out


def decrypt(seed):
    random.seed(seed)

    key = [random.randint(0, 126) for i in range(len(ciphertext))]

    order = shuffle_forward()

    temp = shuffle_backward(ciphertext, order)
    return bytearray([temp[i] ^ key[i] for i in range(len(ciphertext))])


for i in range(startTime, finalTime):
    if(b"ACSI" in decrypt(i)):
        print(decrypt(i))
        break
