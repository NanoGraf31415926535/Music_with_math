import sounddevice as sd
import numpy as np

def generate_bit_sound(number, duration=0.5, sample_rate=44100):
    """Generates a sound based on the binary representation of a number."""

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

        t = np.linspace(0, duration / 4, int(sample_rate * duration / 4), False) #duration/4 because we are playing 4 bits.
        wave = np.sin(2 * np.pi * frequency * t)
        audio = np.concatenate((audio, wave))

    sd.play(audio, sample_rate)
    sd.wait()

# Play sounds for numbers 1 to 10
for i in range(1, 11):
    generate_bit_sound(i)