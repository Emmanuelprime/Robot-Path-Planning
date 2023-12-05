import numpy as np
import matplotlib.pyplot as plt

# Control points for Bézier curve
p0 = np.array([350, 50])    # Starting point
p1 = np.array([350, 100])   # First control point
p2 = np.array([100, 350])   # Second control point
p3 = np.array([50, 350])    # Ending point

# Create a Bézier curve interpolation function
def bezier_curve(t):
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

# Sample points along the Bézier curve
t_values = np.linspace(0, 1, 100)  # Adjust the number of points as needed
smoothed_path = np.array([bezier_curve(t) for t in t_values])

# Plot the smoothed path
plt.plot(smoothed_path[:, 0], smoothed_path[:, 1], 'g-', label='Smoothed Path (Bézier)')
plt.legend()
plt.show()
