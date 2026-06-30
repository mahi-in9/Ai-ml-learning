# from-scratch-ai 🧠

> Building AI from scratch — no shortcuts, no black boxes.
> Every algorithm implemented by hand before using a library.

I'm a MERN stack developer on a 104-week journey to understand and build AI from first principles. This repo is my public learning log — raw code, honest comments, and real benchmarks.

---

## 📁 Week 1 — Foundations

| File | What it does | Key concept |
|---|---|---|
| `week1-matrix-multiply.py` | Matrix multiplication — triple nested loop, no `np.matmul` | Dot product, shape rules |
| `week1-gradient-descent.py` | Find `y = mx + b` from data using gradient descent | Loss function, MSE, update rule |
| `week1-backprop.py` | 2-input network, forward + backward pass by hand | Chain rule, partial derivatives |
| `week1-pytorch-vs-manual.py` | Prove PyTorch autograd = manual math | Gradient verification |
| `week1-benchmark.py` | Speed comparison: scratch vs NumPy vs PyTorch | Why we use libraries |

---

## 🏆 Week 1 Milestone

Manual gradient descent vs PyTorch autograd — losses match to 6 decimal places.

```
Epoch   0: Manual=129.6843  PyTorch=129.6843  diff=0.000000  ✅
Epoch  50: Manual=23.4521   PyTorch=23.4521   diff=0.000000  ✅
Epoch 199: Manual=2.3981    PyTorch=2.3981    diff=0.000001  ✅

🏆 MILESTONE: Manual math = PyTorch autograd
```

---

## ⚡ Benchmarks — Matrix Multiply (50×50, 5 runs)

| Method | Time | Speedup |
|---|---|---|
| Python loops (from scratch) | ~0.8s | 1× (baseline) |
| NumPy `@` operator | ~0.0003s | ~2500× faster |

> Same math. Very different speed. This is why we use libraries.

---

## 📖 Key Lessons From Week 1

1. **Gradient descent = 4 steps**: guess → measure error → find direction → update. That's also how GPT-4 learns.
2. **PyTorch isn't magic**: `.backward()` is the chain rule. I proved it by matching gradients manually.
3. **Shape is everything**: mismatched matrix dimensions = #1 error in deep learning.
4. **NumPy is ~2500× faster** than pure Python loops — compiled C code, no Python overhead.

---

## 🗺️ Roadmap

```
Week 1  ✅  Foundations — NumPy, gradient descent, backprop, PyTorch basics
Week 2  🔄  Neural network layer from scratch
Week 3      Activation functions, loss functions
Week 4      Full network on MNIST
...
Week 104    Ship something real
```

---

## 🛠️ Stack

- Python 3.11+  |  NumPy  |  PyTorch  |  Matplotlib

```bash
pip install numpy torch matplotlib
python week1-matrix-multiply.py
```

---

## 📝 Blog

[Week 1 — I'm a MERN Developer Who Tried to Learn AI](https://medium.com/@mahithegreat19/im-a-mern-developer-0bc90b154d7f)

---
*Building in public. Every line written from memory first, then cleaned up.*
