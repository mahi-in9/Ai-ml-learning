# What

# Without broadcasting (what you'd have to write):

#   matrix = [[1, 2, 3],       bias = [10, 20, 30]
#              [4, 5, 6],
#              [7, 8, 9]]

#   # You'd need a loop:
#   for each row in matrix:
#       add bias to that row

# With broadcasting (what NumPy does automatically):

#   matrix + bias  →  NumPy stretches bias across ALL rows instantly

# why

# Neural network layers always add a bias:

#   output = (weights @ input) + bias

#   weights @ input  shape: (batch=32, neurons=512)
#   bias             shape:           (neurons=512,)

#   NumPy broadcasts bias across all 32 samples automatically.
#   Without broadcasting, you'd need an ugly loop.


# The 3 Broadcasting Rules
# Rule 1: If arrays have different number of dimensions, prepend 1s to the smaller shape. Rule 2: Dimensions of size 1 are stretched to match the other. Rule 3: If sizes differ AND neither is 1 → Error!


import numpy as np

# setup

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

bias = np.array([10, 20, 30]);

result = matrix + bias
print(result)

col_bias = np.array([
    [100],
    [200],
    [300]
])

result2 = matrix + col_bias
print(result2)

a = np.array([1, 2, 3])
b = np.array([10, 20 , 30])


outer = a.reshape(-1, 1) 
print(outer)

# ── Example 4: Normalize a batch (used in batch normalization) ────────────────



batch = np.random.randn(32, 512)
mean = batch.mean(axis=0)
std = batch.std(axis=0)

normalized = (batch - mean) / std
print(normalized.shape)

# common mistakes---------------------

try: 
    bad = np.ones((3, 4)) + np.ones(3,)
except ValueError as e:
    print(f"Broadcasting error: {e}")

fixed = np.ones((3, 4)) + np.ones((3, 1))
print(fixed.shape)

