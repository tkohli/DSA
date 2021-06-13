# Find Common Characters

from collections import Collection
from typing import Counter
words = ["cool", "lock", "cook"]
count = Counter(words[0])
print(count)
for word in (words[1:]):
    test = Counter(word)
    intersection = count & test
    count = count & intersection
    print(count, list(intersection.elements()))
print(count)
