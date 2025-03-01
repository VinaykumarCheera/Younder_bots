def countvowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

print(countvowels("Hello World, I am Vinaykumar"))
