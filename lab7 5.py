import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi,np.pi, 100)

plt.plot(x, np.sin(x))
plt.plot(x, 2*np.sin(x))
plt.plot(x, 2+np.sin(x))
plt.plot(x, np.sin(2*x))
plt.show()