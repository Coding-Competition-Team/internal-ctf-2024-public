import random

# flag = "ACSI{Au_79_196.97_metal}" # 24

flag = "Au_79_196.97_metal"
iflag = [ord(x) for x in flag]
chars = [chr(97+i) for i in range(len(flag))]
print(chars)
random.shuffle(chars)
print(chars)
# 0 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17
# print(iflag[0]**4 + iflag[5]**3 + iflag[6]**2 + iflag[13])

chars = ['d', 'k', 'q', 'p', 'g', 'n', 'r', 'f', 'e', 'a', 'm', 'i', 'l', 'j', 'c', 'b', 'h', 'o']
# d k q p g n r f e a m i l j c b h o
print(f"{chars[0]}**2 + {chars[5]}**3 + {chars[6]}**2 + {chars[13]} = {iflag[0]**2 + iflag[5]**3 + iflag[6]**2 + iflag[13]}")
# print(iflag[1] + iflag[3])
print(f"{chars[1]} + {chars[3]} = {iflag[1] + iflag[3]}")
# print(iflag[0] + iflag [7])
print(f"{chars[0]} + {chars[7]} = {iflag[0] + iflag[7]}")
# print(iflag[8])
print(f"{chars[8]} = {iflag[8]}")
# print(iflag[15] + iflag[16]**2)
print(f"{chars[15]} + {chars[16]}**2 = {iflag[15] + iflag[16]**2}")
# print(iflag[2]**3 + iflag[3])
print(f"{chars[2]}**3 + {chars[3]} = {iflag[2]**3 + iflag[3]}")
# print(iflag[4])
print(f"{chars[4]} = {iflag[4]}")
# print(iflag[16] + iflag[17] + iflag[2])
print(f"{chars[16]} + {chars[17]} + {chars[2]} = {iflag[16] + iflag[17] + iflag[2]}")
# print(iflag[12] + iflag[9])
print(f"{chars[12]} + {chars[9]} = {iflag[12] + iflag[9]}")
# print(iflag[10] + iflag[14] + iflag[8]**2)
print(f"{chars[10]} + {chars[14]} + {chars[8]}**2 = {iflag[10] + iflag[14] + iflag[8]**2}")
# print(iflag[11])
print(f"{chars[11]} = {iflag[11]}")
# print(iflag[13]**3 + iflag[8])
print(f"{chars[13]}**3 + {chars[8]} = {iflag[13]**3 + iflag[8]}")
# print(iflag[6])
print(f"{chars[6]} = {iflag[6]}")

print(f"{chars[5]} = {iflag[5]}")
print(f"{chars[8]} + {chars[2]} = {iflag[8] + iflag[2]}")
print(f"{chars[10]} + {chars[2]} = {iflag[10] + iflag[2]}")
print(f"{chars[1]} + {chars[9]} = {iflag[1] + iflag[9]}")
print(f"{chars[17]} = {iflag[17]}")
print(f"{chars[15]} = {iflag[15]}")
print(f"{chars[11]} + {chars[16]} = {iflag[11] + iflag[16]}")
print(f"{chars[10]} + {chars[1]} = {iflag[10] + iflag[1]}")