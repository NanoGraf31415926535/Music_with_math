import sounddevice as sd
import numpy as np

def generate_bit_sound(number, duration=0.5, sample_rate=44100):
    """Generates a sound based on the binary representation of a number."""

    binary = bin(number)[2:]  # Get binary, remove '0b'
    print(f"Number: {number}, Binary: {binary}")

    audio = np.array([])
    for bit in binary:
        if bit == '1':
            frequency = 880  # High frequency for '1'
        else:
            frequency = 440  # Low frequency for '0'

        t = np.linspace(0, duration / len(binary), int(sample_rate * duration / len(binary)), False) #duration/len(binary) because we are playing len(binary) bits.
        wave = np.sin(2 * np.pi * frequency * t)
        audio = np.concatenate((audio, wave))

    sd.play(audio, sample_rate)
    sd.wait()

# Get user input
while True:
    try:
        user_input = input("Enter a positive integer (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        number = int(user_input)
        if number < 0:
            print("Please enter a positive integer.")
            continue
        generate_bit_sound(number)
    except ValueError:
        print("Invalid input. Please enter a positive integer or 'q'.")