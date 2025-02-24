import numpy as np
import matplotlib.pyplot as plt

def frequency(note_name, octave=4, a4_frequency=440):
    """Calculates the frequency of a musical note."""
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note_name.upper())

    a4_index = notes.index("A")
    semitones_from_a4 = note_index - a4_index + (octave - 4) * 12

    return a4_frequency * (2 ** (semitones_from_a4 / 12))

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a sine wave."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    return t, wave

def visualize_notes(notes, octave=4, duration=0.01, sample_rate=44100):
    """Visualizes sine waves for a list of notes."""
    plt.figure(figsize=(10, 6))  # Adjusted figure size

    for i, note_name in enumerate(notes):
        freq = frequency(note_name, octave)
        t, wave = generate_sine_wave(freq, duration, sample_rate)

        plt.subplot(len(notes), 1, i + 1)  # Create subplots for each note
        plt.plot(t, wave)
        plt.title(f"{note_name}{octave} (Frequency: {freq:.2f} Hz)")
        plt.xlabel("Time (s)")
        if i == 0:
            plt.ylabel("Amplitude")
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add minor grid lines
        plt.xlim(0, duration)
        plt.ylim(-1.2, 1.2)

    plt.tight_layout()
    plt.show()

# Example usage:
selected_notes = ["C", "E", "G", "A"]  # Reduced set of notes
visualize_notes(selected_notes, octave=4)