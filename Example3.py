import sounddevice as sd
import numpy as np

def frequency(note_name, octave=4, a4_frequency=440):
    """Calculates the frequency of a musical note."""
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note_name.upper())

    a4_index = notes.index("A")
    semitones_from_a4 = note_index - a4_index + (octave - 4) * 12

    return a4_frequency * (2 ** (semitones_from_a4 / 12))

def generate_bit_sound(freq, duration, sample_rate=44100):
    """Generates a sound based on the binary representation of a frequency."""

    number = int(freq)
    binary = bin(number)[2:]

    audio = np.array([], dtype=np.float32)  # Corrected line

    for bit in binary:
        if bit == '1':
            bit_frequency = freq * 2
        else:
            bit_frequency = freq / 2

        bit_duration = duration / len(binary)
        t = np.linspace(0, bit_duration, int(sample_rate * bit_duration), False)
        wave = np.sin(2 * np.pi * bit_frequency * t)
        audio = np.concatenate((audio, wave))

    sd.play(audio, sample_rate)
    sd.wait()

def play_note(note_name, duration, octave=4, sample_rate=44100, speed_factor=3.0): #Adjusted speed factor
    """Plays a musical note for a given duration using bit sounds."""
    freq = frequency(note_name, octave)
    generate_bit_sound(freq, duration * speed_factor, sample_rate) #modified duration

# Mario Theme Melody (Simplified)
mario_melody = [
    ("E", 4, 0.15), ("E", 4, 0.15), ("E", 4, 0.3), ("C", 4, 0.15), ("E", 4, 0.3),
    ("G", 4, 0.45), ("G", 3, 0.4),
    ("C", 4, 0.15), ("G", 3, 0.3), ("E", 3, 0.3), ("A", 3, 0.3),
    ("B", 3, 0.3), ("A#", 3, 0.2), ("A", 3, 0.3), ("G", 3, 0.6), ("E", 4, 0.15),
    ("G", 4, 0.15), ("A", 4, 0.2), ("F", 4, 0.15), ("G", 4, 0.15), ("E", 4, 0.3),
    ("C", 4, 0.15), ("D", 4, 0.15), ("B", 3, 0.3), ("C", 4, 0.45), ("G", 3, 0.4),
]

for note, octave, duration in mario_melody:
    play_note(note, duration, octave)