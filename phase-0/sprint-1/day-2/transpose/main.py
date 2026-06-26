# Transpose 

# why? 
# In backpropagation (training neural networks):

#   Forward:  output = W @ input        W shape: (out, in)
#   Backward: gradient = W.T @ delta    W.T shape: (in, out)

# You MUST transpose W to flow gradients backwards.
# Without transpose → backprop doesn't work → AI can't learn.

import numpy as np;

# level - 1: Manual

M = [[1, 2, 3],
     [4, 5, 6]]

rows = len(M)
cols = len(M[0])

# Create empty result: cols rows, rows cols (shape flips!)
MT = [[0] * rows for _ in range(cols)]

for r in range(rows):
    for c in range(cols):
        MT[c][r] = M[r][c]

print(MT)

# level-2 : numPy -------------------

M = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

print(M.T)         # .T property - the standard way
print(M.T.shape)   # -> (3, 2)

# ------ level-3 : Properties of Transpose (senior knowledge) ----------

A = np.random.randn(3, 4)

# (A.T).T == A          Transpose twice = original
print(np.allclose(A.T.T, A))   # true

# (A @ B).T == B.T @ A.T    Order REVERSES on transpose
B = np.random.randn(4, 2)

print(np.allclose((A @ B).T, B.T @ A.T))   #true





