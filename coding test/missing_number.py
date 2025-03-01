def findmissingnumber(lst, n):
    return sum(range(1, n + 1)) - sum(lst)

print(findmissingnumber([1, 2, 3, 5,6,7], 7))
