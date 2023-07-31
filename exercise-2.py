def index_power(numnbers, n):
    for i in numnbers:
        if numnbers.index(i) == n:
            result = i**n
            return result

print(index_power([1,2,3,4],3))