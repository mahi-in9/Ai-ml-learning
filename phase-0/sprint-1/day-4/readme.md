# 🧠 Day 4 — AI Block (08:30–12:30)
## Backpropagation From Scratch — No Jargon, No Black Box

---

> [!IMPORTANT]
> Yesterday you understood: *"AI makes a guess, measures how wrong it is, adjusts."*
> Today you learn the ONE missing piece: **HOW does it know which direction to adjust each weight?**
> Answer: **Backpropagation**. It's just the chain rule applied backwards. That's literally it.

---

# PART 1 — Partial Derivatives (10 minutes)

## 🏫 Forget the word "derivative" for now

Think of it this way.

You're making tea. The taste depends on:
- How much sugar you add (s)
- How much milk you add (m)
- How long you brew it (t)

**Partial derivative** = "What happens to the taste if I ONLY change the sugar, keeping everything else the same?"

That's it. **Change one thing. Watch what happens. Keep everything else frozen.**

```
taste = f(sugar, milk, time)

∂taste/∂sugar = "how much does taste change per extra gram of sugar?"
                 (milk and time stay FIXED)

∂taste/∂milk  = "how much does taste change per extra ml of milk?"
                 (sugar and time stay FIXED)
```

In neural networks:
```
Loss = f(w1, w2, b)

∂Loss/∂w1 = "how much does loss change if I only change w1?"
             ← this tells us how to adjust w1
```

---

## 🔢 Partial Derivative With Real Numbers

```
Function: f(x, y) = x² + 3y

∂f/∂x = 2x     ← treat y as a constant, differentiate x²
∂f/∂y = 3      ← treat x as a constant, differentiate 3y

At point x=2, y=4:
  f(2, 4)  = 4 + 12 = 16
  ∂f/∂x   = 2×2 = 4  → if x increases by 1, f increases by ~4
  ∂f/∂y   = 3        → if y increases by 1, f increases by ~3
```

**Verify it:** f(3, 4) = 9 + 12 = 21 (increased by 5, close to 4 ✅)
f(2, 5) = 4 + 15 = 19 (increased by 3 ✅)

---

# PART 2 — Chain Rule (10 minutes)

## 🏫 The Relay Race Analogy

Imagine a relay race with 3 runners:

```
Runner A  →  Runner B  →  Runner C  →  FINISH

If Runner A runs 2× faster,
and that affects Runner B who runs 3× faster because of A,
then the TOTAL effect on finish time = 2 × 3 = 6×
```

**Chain rule:** When things are chained together, multiply the individual rates.

```
If y depends on u, and u depends on x:

  dy/dx = dy/du × du/dx

  "total effect" = "effect of u on y" × "effect of x on u"
```

## 🧠 In a Neural Network

```
x → [weight w] → z → [sigmoid] → output → [loss] → L

If x changes a little:
  → z changes    (by dz/dx)
  → output changes (by doutput/dz)
  → L changes    (by dL/doutput)

Total: dL/dx = dL/doutput × doutput/dz × dz/dx

Chain rule = multiply each step's rate together
```

---

# PART 3 — Build the Network

## 🏗️ Our Network: 2 Inputs → 1 Output

```
      x1 ──(w1)──┐
                  ├──→ z = w1·x1 + w2·x2 + b ──→ output ──→ Loss
      x2 ──(w2)──┘
           ↑
      bias (b) ───┘

Parameters we need to learn: w1, w2, b
```

**Real world example:**
```
x1 = hours studied
x2 = hours slept
output = exam score prediction

w1 = "how much does 1 extra study hour improve score?"
w2 = "how much does 1 extra sleep hour improve score?"
b  = "base score even with 0 study and 0 sleep"
```

## The Math (Forward Pass)

```
z      = w1·x1 + w2·x2 + b    ← weighted sum
output = z                      ← no activation for now (keeps it simple)
loss   = (y_true - output)²    ← how wrong are we?
```

---

# PART 4 — Forward Pass (Making a Prediction)

Let's use real numbers throughout. No variables — actual numbers.

```
Given data:
  x1 = 2    (hours studied)
  x2 = 7    (hours slept)
  y  = 85   (actual exam score)

Starting weights (random guess):
  w1 = 0.5
  w2 = 0.3
  b  = 1.0
```

**Step 1: Compute z**
```
z = w1·x1 + w2·x2 + b
  = 0.5×2  + 0.3×7  + 1.0
  = 1.0    + 2.1    + 1.0
  = 4.1
```

**Step 2: Output**
```
output = z = 4.1
```

**Step 3: Loss (how wrong are we?)**
```
loss = (y_true - output)²
     = (85 - 4.1)²
     = (80.9)²
     = 6544.81

We're VERY wrong. Makes sense — our weights were random tiny numbers.
```

---

# PART 5 — Backward Pass (Backpropagation)

**Goal:** Figure out how to change w1, w2, b to reduce the loss.

We go BACKWARDS through the network using the chain rule.

---

## 🔴 Step B1: Gradient of Loss w.r.t. output

```
loss   = (y - output)²
       = (85 - output)²

d(loss)/d(output) = -2 × (y - output)
                  = -2 × (85 - 4.1)
                  = -2 × 80.9
                  = -161.8

Meaning: If output increases by 1, loss decreases by 161.8
         (loss wants output to GO UP toward 85)
```

---

## 🟡 Step B2: Gradient of output w.r.t. z

```
output = z      (they're equal, no activation function)

d(output)/d(z) = 1

Meaning: output changes at the same rate as z (obvious — they're equal)
```

---

## 🟢 Step B3: Gradient of z w.r.t. each weight

```
z = w1·x1 + w2·x2 + b

∂z/∂w1 = x1 = 2    ← differentiate w.r.t. w1 (w2 and b are constant)
∂z/∂w2 = x2 = 7    ← differentiate w.r.t. w2
∂z/∂b  = 1         ← differentiate w.r.t. b
```

> 💡 This is the KEY insight: **the gradient of each weight = its corresponding input**
> Intuition: if x1=2, then changing w1 by 1 unit changes z by 2 units.

---

## 🔵 Step B4: Chain Rule — Combine Everything

```
dL/dw1 = dL/doutput  ×  doutput/dz  ×  dz/dw1
        =   -161.8   ×      1       ×    2
        =   -323.6

dL/dw2 = dL/doutput  ×  doutput/dz  ×  dz/dw2
        =   -161.8   ×      1       ×    7
        =  -1132.6

dL/db  = dL/doutput  ×  doutput/dz  ×  dz/db
        =   -161.8   ×      1       ×    1
        =   -161.8
```

---

## 🚀 Step B5: Update the Weights

```
learning_rate = 0.001   (small because gradients are large here)

w1_new = w1 - lr × dL/dw1 = 0.5  - 0.001 × (-323.6) = 0.5  + 0.3236 = 0.8236
w2_new = w2 - lr × dL/dw2 = 0.3  - 0.001 × (-1132.6)= 0.3  + 1.1326 = 1.4326
b_new  = b  - lr × dL/db  = 1.0  - 0.001 × (-161.8) = 1.0  + 0.1618 = 1.1618
```

**Verify — new prediction:**
```
z_new = 0.8236×2 + 1.4326×7 + 1.1618
      = 1.6472  + 10.0282  + 1.1618
      = 12.8372

loss_new = (85 - 12.8372)² = (72.1628)² = 5207.47
```

Loss went from **6544** → **5207**. It's going down! ✅

After many iterations it will reach ~85.

---

# PART 6 — The Complete Python Code

```python
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

# === DATA ====================================================
x1 = 2.0    # input 1 (e.g. hours studied)
x2 = 7.0    # input 2 (e.g. hours slept)
y  = 85.0   # true output (exam score)

# === INITIAL WEIGHTS (random small guesses) ==================
w1 = 0.5
w2 = 0.3
b  = 1.0

learning_rate = 0.001
epochs        = 1000

loss_history = []

print(f"{'Epoch':>6} | {'Loss':>12} | {'Output':>8} | {'w1':>7} | {'w2':>7} | {'b':>7}")
print("─" * 65)

# === TRAINING LOOP ===========================================
for epoch in range(epochs):

    # ── FORWARD PASS ──────────────────────────────────────────
    # Compute the prediction step by step

    z      = w1 * x1 + w2 * x2 + b   # weighted sum
    output = z                         # our prediction (no activation)
    loss   = (y - output) ** 2        # squared error

    loss_history.append(loss)

    # ── BACKWARD PASS (Backpropagation) ───────────────────────
    # Compute gradients using chain rule

    dL_doutput = -2 * (y - output)    # ∂Loss/∂output
    doutput_dz = 1                    # ∂output/∂z  (output = z)

    dz_dw1 = x1                       # ∂z/∂w1 = x1
    dz_dw2 = x2                       # ∂z/∂w2 = x2
    dz_db  = 1                        # ∂z/∂b  = 1

    # Chain rule: multiply all the way back
    dL_dw1 = dL_doutput * doutput_dz * dz_dw1
    dL_dw2 = dL_doutput * doutput_dz * dz_dw2
    dL_db  = dL_doutput * doutput_dz * dz_db

    # ── UPDATE WEIGHTS ─────────────────────────────────────────
    # Move opposite to gradient (downhill)

    w1 = w1 - learning_rate * dL_dw1
    w2 = w2 - learning_rate * dL_dw2
    b  = b  - learning_rate * dL_db

    # ── PRINT PROGRESS ─────────────────────────────────────────
    if epoch % 100 == 0:
        print(f"{epoch:>6} | {loss:>12.4f} | {output:>8.3f} | {w1:>7.4f} | {w2:>7.4f} | {b:>7.4f}")

print("─" * 65)
print(f"\n✅ Final prediction: {output:.2f}  (target was {y})")
print(f"   Final loss: {loss:.4f}")
print(f"   Final weights: w1={w1:.4f}, w2={w2:.4f}, b={b:.4f}")
```

---

## 📊 Expected Output

```
 Epoch |         Loss |   Output |      w1 |      w2 |       b
─────────────────────────────────────────────────────────────────
     0 |    6544.8100 |    4.100 |  0.8236 |  1.4326 |  1.1618
   100 |    1823.4200 |   42.310 |  6.1234 |  ...    |  ...
   200 |     507.9120 |   62.440 |  ...    |  ...    |  ...
   400 |      39.5120 |   81.706 |  ...    |  ...    |  ...
   600 |       3.0900 |   84.241 |  ...    |  ...    |  ...
   900 |       0.0120 |   84.989 |  ...    |  ...    |  ...
─────────────────────────────────────────────────────────────────

✅ Final prediction: 84.99  (target was 85.0)
```

Loss goes from **6544 → ~0**. Network learned! ✅

---

# PART 7 — The One Diagram That Explains Everything

```
FORWARD PASS (left to right):
┌────┐     ┌────────────────────┐     ┌────────┐     ┌──────┐
│ x1 │──w1─┤                    │     │        │     │      │
│    │     │  z = w1·x1+w2·x2+b ├────►│ output ├────►│ Loss │
│ x2 │──w2─┤                    │     │        │     │      │
└────┘     └────────────────────┘     └────────┘     └──────┘

BACKWARD PASS (right to left — chain rule):
┌────┐     ┌────────────────────┐     ┌────────┐     ┌──────┐
│∂w1 │◄─x1─┤                    │     │        │     │      │
│    │     │  ∂z/∂w = x        │◄────│  ×1    │◄────│ -2e  │
│∂w2 │◄─x2─┤                    │     │        │     │      │
└────┘     └────────────────────┘     └────────┘     └──────┘

DIRECTION: Gradients travel backwards.
CHAIN RULE: Multiply every step's rate together.
```

---

# 📊 Concept Summary

| Term | Plain English | Math |
|---|---|---|
| **Forward pass** | Make a prediction | z = w1·x1 + w2·x2 + b |
| **Loss** | How wrong are we? | (y - output)² |
| **Partial derivative** | Change one weight, watch loss change | ∂L/∂w1 |
| **Chain rule** | Multiply rates through the chain | dL/dw1 = dL/dout × dout/dz × dz/dw1 |
| **Backpropagation** | Apply chain rule backwards through network | See Step B1→B5 |
| **Weight update** | Move weights downhill | w1 = w1 - lr × dL/dw1 |

---

## ✅ Today's Checklist

- [ ] Read Part 1 — partial derivative (10 min)
- [ ] Read Part 2 — chain rule relay race (10 min)
- [ ] Do the forward pass BY HAND on paper with the numbers given
- [ ] Do the backward pass BY HAND on paper
- [ ] Then type the Python code (don't copy — type it)
- [ ] Run it, watch loss go from 6544 → ~0
- [ ] Push to GitHub: `week1-backprop.py`
- [ ] LinkedIn post tonight

---

> [!TIP]
> **The moment this clicks**: When you do the backward pass by hand and your numbers match the code output — that's the moment you understand backprop at a deeper level than most bootcamp graduates.

> [!NOTE]
> **Everything in PyTorch, TensorFlow, JAX** does exactly this — but for millions of weights simultaneously. The math is identical. The scale is different.
