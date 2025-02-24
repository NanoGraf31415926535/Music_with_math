import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a sine wave and plots it."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)  # Simplified: A=1, phase=0
    return t, wave

def visualize_sine_wave(frequency, duration, sample_rate=44100, zoom_duration=0.1):
    """Generates and visualizes a sine wave, with a zoom."""
    t, wave = generate_sine_wave(frequency, duration, sample_rate)

    plt.figure(figsize=(12, 6))

    # Full wave plot
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
    plt.plot(t, wave)
    plt.title(f"Sine Wave (Frequency: {frequency} Hz, Duration: {duration} s)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Zoomed-in plot
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
    zoom_start = 0  # Start of zoom
    zoom_end = zoom_duration # End of zoom
    zoom_indices = (t >= zoom_start) & (t <= zoom_end) #filter out the points we do not want.

    plt.plot(t[zoom_indices], wave[zoom_indices])
    plt.title(f"Zoomed-in Sine Wave (First {zoom_duration} s)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout() #prevents overlap of plots.
    plt.show()

# Example usage:
frequency = 1  # 1 Hz frequency
duration = 2  # 2 seconds duration
visualize_sine_wave(frequency, duration)

frequency = 440 # A4
duration = 0.01 # short duration, to show a few waves.
visualize_sine_wave(frequency, duration, zoom_duration = 0.005)

frequency = 880 # A5
duration = 0.01 # short duration, to show a few waves.
visualize_sine_wave(frequency, duration, zoom_duration = 0.005)