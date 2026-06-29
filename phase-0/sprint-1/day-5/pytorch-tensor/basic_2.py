import torch

t1 = torch.tensor([1.0, 2.0, 3.0])
t2 = torch.zeros(3, 4)
t3 = torch.ones(2, 3)
t4 = torch.randn(3, 3)
t5 = torch.arange(0, 10, 2)

print(t2.shape)
print(t2.shape[0])

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print(a+b)
print(a*b)
print(a@b)

# converting between numpy and pytorch

import numpy as np

np_arr = np.array([1.0, 2.0, 3.0])
torch_t = torch.from_numpy(np_arr)
back_to_np = torch_t.numpy()

w = torch.tensor(2.0, requires_grad=True)

y = w ** 3 + 4 * w

y.backward()

print(w.grad)

w.grad.zero_()




