import random

for f in range(0, 100):
    file = open(f"./in/{f}.in",'w')
    n = random.randint(2, 10000)
    
    e = random.randint(1, 10000)
    
    solve = False
    if random.randint(0, 20) != 0:
        solve = True
        e += (n - 1)
    file.write(f"{n} {e}\n")
    
    if solve:
        e = e - (n - 1)
    
    # edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    # random.shuffle(edges)
    
    # adj = [[] for _ in range(n)]
    # for _ in range(e):
    #     l, r = edges.pop()
    #     dist = random.randint(1, 1000000)
    #     file.write(f"{l} {r} {dist}\n")
    #     adj[l].append(r)
    #     adj[r].append(l)
    
    edge_set = set()
    # chosen = []
    # for i in range(n):
    #     for j in range(i, n):
    #         edge_set.append((i, j))
    
    for _ in range(e):
        l, r = random.sample(range(n), 2)
        while (l, r) in edge_set:
            l, r = random.sample(range(n), 2)
            # print(f"{l} {r}")
        # while True:
        #     l = random.randint(0, n - 1)
        #     r = random.randint(0, n - 1)
        #     if l != r and (l, r) not in edge_set and (r, l) not in edge_set:
        #         break
        # while True:
        #     c = random.randint(0, len(edge_set))
        #     if c not in chosen:
        #         l, r = edge_set[c]
        #         chosen.append[c]
        #         break
        dist = random.randint(1, 1000000)
        file.write(f"{l} {r} {dist}\n")
        edge_set.add((l, r))
        edge_set.add((r, l))
    
    if solve:
        for i in range(n - 1):
            l = i
            r = i + 1
            if (l, r) in edge_set or (r, l) in edge_set:
                continue
            dist = random.randint(1, 1000000)
            file.write(f"{l} {r} {dist}\n")
            edge_set.add((l, r))
            edge_set.add((r, l))
    
    file.close()