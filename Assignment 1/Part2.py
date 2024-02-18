import numpy as np
import matplotlib.pyplot as plt

def sineWave(t, a, f, theta):   # function to return the sine wave
    return a * np.sin(2 * np.pi * f * t + theta)

t = np.linspace(-1, 1, 1000) # Generate t values between -1 and 1

# Define parameters
parameters = [
    {"a": 1, "f": 1, "theta": 0},
    {"a": 1, "f": 2, "theta": 0},
    {"a": 2, "f": 1, "theta": 0},
    {"a": 1, "f": 1, "theta": np.pi / 2}]


#create plot
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i, ax in enumerate(axs.flatten()):
    params = parameters[i]
    y = sineWave(t, params["a"], params["f"], params["theta"])
    ax.plot(t, y)
    ax.set_title(f"a={params['a']}, f={params['f']}, theta={params['theta']}")
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Amplitude')

# Adjust layout to prevent overlapping titles
plt.tight_layout()

# Show the plot
plt.show()

# the graph is displayed once the file is run