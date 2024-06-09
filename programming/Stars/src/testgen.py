import random

for f in range(0, 100):
    file = open(f"./in/{f}.in",'w')
    n = random.randint(1, 1000000)
    s = random.randint(1, 50000)
    
    file.write(f"{n} {s}\n")
    
    t = [random.randint(1, 1000000) for _ in range(n)]
    ts = " ".join(str(i) for i in t)
    file.write(f"{ts}\n")
    
    for i in range(s):
        file.write(f"{random.randint(0, n - 1)}\n")
    
    file.close()