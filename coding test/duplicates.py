def removeduplicates(lst):
    return list(dict.fromkeys(lst))

print(removeduplicates([1, 2, 2, 3, 4, 4, 5,99,9,9,0,1,2,3]))
