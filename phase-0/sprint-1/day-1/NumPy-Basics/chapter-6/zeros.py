
import numpy as np

zeros = np.zeros((3, 4))

print(zeros.shape)
print(zeros)

ones = np.ones((2, 5))

# identify matrix
identity = np.eye(4)
print(identity)

# range of numbers
arange = np.arange(0, 10, 2);
print(arange);

# evenly space number
linspace = np.linspace(0, 1, 5)
print(linspace)

random = np.random.rand(3, 3)
normal = np.random.randn(3, 3)

print(random)
print(normal)

