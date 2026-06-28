import numpy as np


# ─────────────────────────────────────────────────
# THE NETWORK
# ─────────────────────────────────────────────────
#
#  x1 ──(w1)──┐
#              ├──→ z = w1·x1 + w2·x2 + b ──→ output ──→ loss
#  x2 ──(w2)──┘
#        (b) ──┘
#
# ─────────────────────────────────────────────────

# Data

x1 = 2.0   # input 1
x2 = 5.9   # input 2
y = 85.0    # true output

# inital guess------------------------

w1 = 0.5
w2 = 0.3
b = 1.0

learning_rate = 0.001
epochs = 1000

loss_history = []

print(f"{'Epoch':>6} | {'Loss':>12} | {'Output':>8} | {'w1':>7} | {'w2':>7} | {'b':>7}")
print("─" * 65)

# training loop

for epoch in range(epochs):
    # forward pass
    # compute the predictions step by step

    z = w1*x1 + w2*x2 + b  #weighted sum
    output = z
    loss = (y - output) ** 2

    loss_history.append(loss)

    # Backward pass
    # compute gredients using chain rule

    dl_doutput = -2 * (y - output)
    doutput_dz = 1

    dz_dw1 = x1
    dz_dw2 = x2
    dz_db = 1

    # chain rule: multiply all the rule back

    dz_dw1 = dl_doutput * doutput_dz * dz_dw1
    dz_dw2 = dl_doutput * doutput_dz * dz_dw2
    dz_db = dl_doutput * doutput_dz * dz_db

    # # Update weights
    # # move opposite to gradient

    # w1 = w1 - learning_rate * dl_dw1
    # w1 = w2 - learning_rate * dl_dw2
    # b = b - learning_rate * dl_db

    if epoch % 100 == 0:
        print(f"{epoch:>6} | {loss:>12.4f} | {output:>8.3f} | {w1:>7.4f} | {w2:>7.4f} | {b:7.4f}");

print("—", 65)
print(f"\n✅ Final prediction: {output:.2f}  (target was {y})")
print(f"   Final loss: {loss:.4f}")
print(f"   Final weights: w1={w1:.4f}, w2={w2:.4f}, b={b:.4f}")


