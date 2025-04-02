import numpy as np
import matplotlib.pyplot as plt

def square_wave(x):
    return np.where(np.mod(x, 2*np.pi) < np.pi, 1, -1)

def fourier_approx(x, N):
    return sum((4/np.pi) * np.sin((2*k-1)*x)/(2*k-1) for k in range(1, N+1))

x = np.linspace(-np.pi, np.pi, 1000)
plt.plot(x, square_wave(x), 'r', label="Square Wave")
plt.plot(x, fourier_approx(x, 100), 'b--', label="N=100")
plt.legend()
plt.show()
plt.savefig("plot.jpg", dpi=300)  # Higher resolution
