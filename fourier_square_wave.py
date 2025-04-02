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
