# Matrix

# A (2×2):            B (2×2):
# [[1, 2],            [[5, 6],
#  [3, 4]]             [7, 8]]

# C = A × B:

# C[0][0] = dot( [1,2], [5,7] ) = 1×5 + 2×7 = 19
# C[0][1] = dot( [1,2], [6,8] ) = 1×6 + 2×8 = 22
# C[1][0] = dot( [3,4], [5,7] ) = 3×5 + 4×7 = 43
# C[1][1] = dot( [3,4], [6,8] ) = 3×6 + 4×8 = 50

# Result:
# [[19, 22],
#  [43, 50]]


#      A            B            C
#   (m × k)  ×  (k × n)  =  (m × n)
#           ↑↑↑
#    These MUST match!
#    If they don't → Error

# Example:
#   (3 × 2) × (2 × 4) = (3 × 4)   ✅
#   (3 × 2) × (3 × 4) = ERROR      ❌  (2 ≠ 3)


import numpy as np

def matmul_scratch(A, B):

    """
    Matrix multiplication without np.matmul or np.dot.
    Uses the triple nested loop (the most fundamental form).
    A: shape (m, k)
    B: shape (k, n)
    Returns C: shape (m, n)
    """
    
    m = len(A)
    k = len(A[0])
    k2 = len(B)
    n = len(B[0])

    if k != k2:
        raise ValueError (
            f"Shape mismatch!\n"
            f" A: ({m} x {k})\n"
            f" B: ({k2} x {n})\n"
            f" A's cols ({k}) must equal B's rows({k2})"
        )
    
    # initialize output C with zero ------------

    C = [[0.0] * n for _ in range(m) ]    #shape (m x n)

    # ── Triple loop: the heart of matrix multiply ────────────

    for i in range(m):
        for j in range(n):
            total = 0.0
            for p  in range(k):
                total += A[i][p] * B[p][j]
            C[i][j] = total
    return C



# Test 1: simple 2x2

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = matmul_scratch(A, B)
print("C from scratch", C)

# -> [[19.0, 22.0], [43.0, 50.0]]

# verify against numPy

C_np = (np.array(A) @ np.array(B)).tolist()
print("C from NumPy: ", C_np)
print("Match:", np.allclose(C, C_np))


# Test 2: Non-square (3x2) x (2x4) -> (3x4)

A2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
        
B2 = [
    [7, 8 , 9, 10],
    [11, 12, 13, 14]
]    

C2 = matmul_scratch(A2, B2);

print("\n C2 (3x4) from sratch:")
for row in C2:
    print(" ", row)

print("Rows:", len(C2), "Cols:", len(C2[0]))

# Test3: shape mismtach error handling

try:
    matmul_scratch([[1, 2, 3]], [[1, 2], [3, 4]]);
except ValueError as e:
    print("\n Expected error carught:")
    print(e)



# ═══════════════════════════════════════════════════════════
# SENIOR INSIGHT: Why is our version slow?
# ═══════════════════════════════════════════════════════════


import timeit

size = 30
A_big = np.random.randn(size, size).tolist()
B_big = np.random.randn(size, size).tolist()

t_scratch = timeit.timeit(lambda: matmul_scratch(A_big, B_big), number=5)

A_np = np.array(A_big)
B_np = np.array(B_big)
t_numpy = timeit.timeit(lambda: A_np @ B_np, number=5)

print(f"\n⚡ Benchmark (30x30 matrix, 5 runs:)")
print(f" Scratch: {t_scratch:.3f}s")
print(f" NumPy: {t_numpy:.5f}s")
print(f" NumPy is ~{t_scratch/t_numpy:.0f}x faster")


# The triple loop maps directly to the math:

#   for i in range(m):       ← "for each output ROW"
#     for j in range(n):     ← "for each output COLUMN"
#       for p in range(k):   ← "compute the dot product"
#         C[i][j] += A[i][p] * B[p][j]

# Complexity: O(m × n × k) — for large matrices this is SLOW in Python.

# NumPy's solution:
#   ✓ Compiled C code (no Python interpreter overhead)
#   ✓ BLAS routines (decades-optimized math libraries)
#   ✓ SIMD: one CPU instruction processes 8 numbers simultaneously
#   ✓ Cache-aware: reads memory in optimal order
#   ✓ On GPU: 10,000 cores do it in parallel (CUDA)

