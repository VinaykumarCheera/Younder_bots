def second_largest(lst):
    return sorted(set(lst))[-2]

print(second_largest([10, 20, 4, 45, 99,56,34,12]))
