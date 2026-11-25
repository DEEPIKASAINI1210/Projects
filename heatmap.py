import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data=np.random.rand(12,12)
plt.imshow(data,cmap='viridis')
plt.colorbar()
plt.title("Heatmap")
plt.xlabel("X-xis")
plt.ylabel("y-xis")
plt.show()
