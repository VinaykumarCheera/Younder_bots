from collections import Counter

def mostfrequent(lst):
    return Counter(lst).most_common(1)[0][0]

print(mostfrequent([1, 2, 2, 3, 3, 3, 4,5]))
