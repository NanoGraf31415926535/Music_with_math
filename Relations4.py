import numpy as np
import matplotlib.pyplot as plt

def generate_bit_sound(number, duration=0.5, sample_rate=44100):
    """Generates a sound based on the binary representation of a number and plots it."""

    if not 1 <= number <= 10:
        raise ValueError("Number must be between 1 and 10.")

    binary = bin(number)[2:].zfill(4)  # Get binary, remove '0b', pad to 4 bits
    print(f"Number: {number}, Binary: {binary}")

    audio = np.array([])
    for bit in binary:
        if bit == '1':
            frequency = 880  # High frequency for '1'
        else:
            frequency = 440  # Low frequency for '0'

        t = np.linspace(0, duration / 4, int(sample_rate * duration / 4), False)  # duration/4 because we are playing 4 bits.
        wave = np.sin(2 * np.pi * frequency * t)
        audio = np.concatenate((audio, wave))

    # Plot the audio
    time = np.linspace(0, duration, len(audio), False) # Corrected line
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio)
    plt.title(f"Sound Representation of {number} (Binary: {binary})")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

# Play sounds for numbers 1 to 10 and plot them
for i in range(1, 11):
    generate_bit_sound(i)