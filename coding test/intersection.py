def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

print(list_intersection([1, 2, 3,5,6,7], [2, 3, 4,9,0]))
