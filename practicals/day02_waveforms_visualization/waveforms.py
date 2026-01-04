import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal

fs = 10000
t = np.linspace(0, 0.01, fs)
f = 100

sine = np.sin(2 * np.pi * f * t)
square = signal.square(2 * np.pi * f * t)
triangle = signal.sawtooth(2 * np.pi * f * t, 0.5)

plt.figure()
plt.plot(t, sine, label="sine")
plt.plot(t, square, label="square")
plt.plot(t, triangle, label="triangle")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Waveform Comparison")
plt.show()