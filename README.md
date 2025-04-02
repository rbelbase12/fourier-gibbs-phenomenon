# Fourier Series Animation: Gibbs Phenomenon Visualization

A Python project demonstrating how Fourier series approximate a square wave, including the Gibbs phenomenon (overshoot near discontinuities).


## 📖 Background  
The square wave function (odd periodic extension) is defined as:
![Equation](https://quicklatex.com/cache3/7d/ql_48c0f5cfa0558e7b74872db966f8197d_l3.png)

The Fourier series of a square wave is given by:
![Equation](https://quicklatex.com/cache3/ab/ql_f2723aee1f3cceca8e7e71fcfd984cab_l3.png)

Despite increasing \( N \), the approximation exhibits **Gibbs phenomenon**—persistent overshoots (~9%) near jumps.
| **Graph of Partial Fourier Sum $S_5(x)$**  | **Graph of Partial Fourier Sum $S_{20}(x)$**  |
|-------------|-------------|
| !![Image 1](./assets/sqwaven5.jpg) | !![Image 2](./assets/sqwaven20.jpg) |
| **Graph of Partial Fourier Sum $S_{50}(x)$**  | **Graph of Partial Fourier Sum $S_{100}(x)$**  |
| !!![Image 3](./assets/sqwaven50.jpg) | !![Image 4](./assets/sqwaven100.jpg) |

## 🎥 Demo  
![Demo GIF](assets/fourier_animation.gif)
**Key Observations**

Initial Approximation (Low N)

With few terms (e.g., N=5), the Fourier series is a wavy approximation of the square wave.

The curve struggles to match the sharp jump, resulting in large oscillations.

Increasing Terms (Higher N)

As N increases (e.g., N=50), the approximation improves in smooth regions.

However, near the discontinuity (e.g., x=0 or x=π), an overshoot appears.

The overshoot does not disappear even as N → ∞ (it stabilizes at ~9% of the jump height).

Gibbs Overshoot Persists

The peak overshoot remains at ~1.08949 (for a jump from −1 to +1).

The width of the overshoot shrinks as N increases, but the height stays constant.

## 🛠️ Setup  
1. Clone the repo:
   ```bash
   git clone https://github.com/rbelbase12/fourier-gibbs-phenomenon.git
## Python Code for Fourier Series Approximation Animation
```python
# Example: Plot Gibbs phenomenon
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML  # Required for Colab

# Define the square wave
def square_wave(x):
    return np.where((x >= 0) & (x < np.pi), 1, -1)

# Define the Fourier partial sum
def fourier_sum(x, N):
    s = 0
    for n in range(1, N+1):
        s += np.sin((2*n-1)*x) / (2*n-1)
    return (4/np.pi) * s

# Set up the x-axis
x = np.linspace(-np.pi, np.pi, 1000)
y_true = square_wave(x)

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Fourier Approximation of Square Wave")
line_true, = ax.plot(x, y_true, 'r-', label="Square Wave", linewidth=2)
line_approx, = ax.plot([], [], 'b-', label="Fourier Sum", linewidth=2)
ax.legend(loc="upper right")
ax.grid(True)

# Animation update function
def update(N):
    y_approx = fourier_sum(x, N)
    line_approx.set_data(x, y_approx)
    ax.set_title(f"Fourier Approximation (N = {N})")
    return line_approx,

# Create the animation
ani = FuncAnimation(
    fig,
    update,
    frames=range(1, 100),  # Try increasing to 100 for smoother results
    blit=True,
    interval=100  # Delay between frames (ms)
)

# Render in Colab
plt.close()  # Prevents duplicate display
HTML(ani.to_jshtml())  # Ensures animation plays in Colab
ani.save("fourier_animation.gif", writer="pillow", fps=10)  # Requires pillow
# ani.save("fourier_animation.mp4", writer="ffmpeg", fps=10)  # Requires ffmpeg
```
## References
1. Gibbs, J. W. (1899). *Fourier Series*. (https://www.nature.com/articles/059606a0.pdf)

