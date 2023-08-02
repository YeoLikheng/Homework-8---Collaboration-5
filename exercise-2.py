def index_power(numnbers, n):
    for i in numnbers:
        if numnbers.index(i) == n:
            result = i**n
            return result
        elif n not in range(len(numnbers)):
            return -1

