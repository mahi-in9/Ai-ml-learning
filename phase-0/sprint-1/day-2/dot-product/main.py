import numpy as np

# level 1 - manual

a = [1, 2, 3]
b = [4, 5, 6]

result = 0;

for i in range(len(a)):
    result += a[i] * b[i]

print (result)

# level 2 - numpy


a = np.array([1 , 2, 3]);
b = np.array([4, 5 , 6])

print(np.dot(a, b));
print( a @ b)   # same modern way to write


# ---level 3 - What maks two vecotrs "similar"----

# Dot product is related to cosine similarity used in ChatGPT embeddings!
# High dot product = vectors point in same direction = similar concepts
# Zero dot product = vectors are perpendicular = completely unrelated

v1 = np.array([1, 0])  # points right
v2 = np.array([0, 1])  # points up
v3 = np.array([1, 0])  # points right

print(np.dot(v1, v2))  # -> 0 perpendicular unrelated
print(np.dot(v1, v3))  # -> 1 (same direction - identical)



