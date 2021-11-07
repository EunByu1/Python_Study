def euclid(p,q):
    if q == 0:
        return p
    else:   
        return euclid(q, p%q)

print(euclid(10,5))
