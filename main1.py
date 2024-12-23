import matplotlib.pyplot as mat
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
mat.plot(x, y)
mat.show()