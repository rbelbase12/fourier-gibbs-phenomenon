# Fourier Series Animation: Gibbs Phenomenon Visualization

A Python project demonstrating how Fourier series approximate a square wave, including the Gibbs phenomenon (overshoot near discontinuities).

## 🎥 Demo  
fourier_animation.gif

## 📖 Background  
The Fourier series of a square wave is given by:
\[
S_N(x) = \frac{4}{\pi} \sum_{n=1}^{N} \frac{\sin((2n-1)x)}{2n-1}
\]
Despite increasing \( N \), the approximation exhibits **Gibbs phenomenon**—persistent overshoots (~9%) near jumps.

## 🛠️ Setup  
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/fourier-gibbs-phenomenon.git
