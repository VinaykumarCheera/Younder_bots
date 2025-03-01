def first_non_repeating_chr(s):
    from collections import Counter
    count = Counter(s)
    for chr in s:
        if count[chr] == 1:
            return chr
    return None

print(first_non_repeating_chr("swissabcdes"))
