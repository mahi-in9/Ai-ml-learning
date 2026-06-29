# Data: x = [0..10], y = 2x + 5 + noise Starting weights: m=0.0, b=0.0 Learning rate: 0.01 Epochs: 10 

import numpy as np 
import torch

np.random.seed(42)
torch.manual_seed(42)

N = 100
x_np = np.linspace(0, 10, N)
noise = np.random.randn(N) * 1.5
y_np = 2*x_np + 5 + noise

# method-1 : manual

m_manual = 0.0
b_manual = 0.0
lr = 0.01

manual_losses = []

for epoch in range(10):
    preds = m_manual * x_np + b_manual    
    errors = y_np - preds
    loss = np.mean(errors ** 2)
    manual_losses.append(loss)

    dm = (-2 / N * np.sum(x_np * errors))
    db = (-2/N) * np.sum(errors)

    #Update

    m_manual -= lr * dm
    b_manual -= lr * db

    print(f"[MANUAL] EPOCH {epoch} | Loss: {loss:.4f} | m: {m_manual:.4f}")
print()

# method-2: PYTORCH AUTOGRAD

x_t = torch.tensor(x_np, dtype=torch.float32)
y_t = torch.tensor(y_np, dtype=torch.float32)

m_torch = torch.tensor(0.0, requires_grad=True)
b_torch = torch.tensor(0.0, requires_grad=True)

pytorch_losses = []

for epoch in range(10):
    preds = m_torch * x_t + b_torch
    loss = torch.mean((y_t - preds) ** 2)
    pytorch_losses.append(loss.item())


    loss.backward()

    with torch.no_grad():
        m_torch -= lr*m_torch.grad
        b_torch -= lr* b_torch.grad

    m_torch.grad.zero_()
    b_torch.grad.zero_()

    print(f"[PYTORCH] EPOCH {epoch} | LOSSS: {pytorch_losses[-1]:.4f} | m: {m_torch:.4f} | b: {b_torch:.4f}")

print()

# verify

print("=" * 55)
print(" VERIFICATION: Manual vs Pytorch")
print("=" * 55)

all_match = True
for i in range(10):
    diff = abs(manual_losses[i] - pytorch_losses[i])
    match = "✅" if diff < 0.001 else "❌"
    if diff >= 0.001: 
        all_match = False
        print(f" Epoch {i}: Manual={manual_losses[i]:.4f} Pytorch={pytorch_losses[-1]:.4f} diff={diff:.6f} {match}")

print("=" * 55)
if all_match:
    print(" 🏆 MILESTONE ACHIEVED: All losses match perfectly!")
else:
    print(" ❌ Mismatch detected — check your formulas!")

