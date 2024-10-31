import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2, 100)
y = np.sin(2*x)
plt.plot(x, y)
plt.xlim(0, 2*np.pi)
plt.title('sin(2x)')
plt.savefig('sin(2x).jpg')
plt.show()
