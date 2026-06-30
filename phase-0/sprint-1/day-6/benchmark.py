"""
Week 1 — Speed Benchmark
Compares: Python scratch vs NumPy vs PyTorch
Shows WHY we use libraries instead of writing everything from scratch.
"""

import numpy as np
import torch
import timeit

SIZE = 50    # 50×50 matrix
RUNS = 5

print("=" * 55)
print(f"  Matrix Multiply Benchmark ({SIZE}×{SIZE}, {RUNS} runs)")
print("=" * 55)

# ── Method 1: Pure Python (your scratch implementation) ──────
A_list = np.random.randn(SIZE, SIZE).tolist()
B_list = np.random.randn(SIZE, SIZE).tolist()

def matmul_scratch(A, B):
    m, k, n = len(A), len(A[0]), len(B[0])
    C = [[0.0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for p in range(k):
                C[i][j] += A[i][p] * B[p][j]
    return C

t_scratch = timeit.timeit(lambda: matmul_scratch(A_list, B_list), number=RUNS)

# ── Method 2: NumPy ───────────────────────────────────────────
A_np = np.array(A_list)
B_np = np.array(B_list)

t_numpy = timeit.timeit(lambda: A_np @ B_np, number=RUNS)

# ── Method 3: PyTorch ─────────────────────────────────────────
A_pt = torch.tensor(A_list, dtype=torch.float32)
B_pt = torch.tensor(B_list, dtype=torch.float32)

t_pytorch = timeit.timeit(lambda: A_pt @ B_pt, number=RUNS)

# ── Results ───────────────────────────────────────────────────
print(f"\n  {'Method':<20} {'Time':>10} {'Speedup':>10}")
print(f"  {'-'*42}")
print(f"  {'Python scratch':<20} {t_scratch:>9.4f}s {'1×':>10}")
print(f"  {'NumPy (@)':<20} {t_numpy:>9.5f}s {t_scratch/t_numpy:>9.0f}×")
print(f"  {'PyTorch (@)':<20} {t_pytorch:>9.5f}s {t_scratch/t_pytorch:>9.0f}×")

print(f"\n  NumPy is ~{t_scratch/t_numpy:.0f}× faster than Python loops")
print(f"  This gap grows with matrix size — for 1000×1000: ~1,000,000×")
print("=" * 55)

# ── Verify all three give same answer ─────────────────────────
C_scratch = np.array(matmul_scratch(A_list, B_list))
C_numpy   = A_np @ B_np
C_pytorch = (A_pt @ B_pt).numpy()

print(f"\n  Correctness check:")
print(f"  Scratch vs NumPy:   {np.allclose(C_scratch, C_numpy, atol=1e-4)} ✅")
print(f"  NumPy vs PyTorch:   {np.allclose(C_numpy, C_pytorch, atol=1e-4)} ✅")
print(f"\n  Same result. Different speed. This is why libraries exist.")