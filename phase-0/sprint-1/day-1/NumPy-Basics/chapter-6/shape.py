# grids
# 💬 Shape is EVERYTHING in AI. When you build a neural network:

# Input image might be shape (batch=32, height=224, width=224, channels=3)
# A weight matrix might be (768, 3072)
# Mismatched shapes = the #1 error in deep learning!


import numpy as np;


arr1d = np.array([1, 2, 3, 4, 5]);
arr2d = np.array([[1, 2, 3], [4, 5, 6]]);
arr3d = np.zeros((2, 4, 3))

print(arr1d.shape)
print(arr2d.shape)
print(arr3d.shape)



