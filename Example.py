import sounddevice as sd
import numpy as np

def frequency(note_name, octave=4, a4_frequency=440):
    """Calculates the frequency of a musical note."""
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note_name.upper())

    a4_index = notes.index("A")
    semitones_from_a4 = note_index - a4_index + (octave - 4) * 12

    return a4_frequency * (2 ** (semitones_from_a4 / 12))

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a sine wave at a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    return wave

def play_note(note_name, duration, octave=4, sample_rate=44100):
    """Plays a musical note for a given duration."""
    freq = frequency(note_name, octave)
    wave = generate_sine_wave(freq, duration, sample_rate)
    audio = wave  # sounddevice expects -1 to 1 range
    sd.play(audio, sample_rate)
    sd.wait()

# Example usage:
play_note("C", 0.5, 4)  # Play C4 for 0.5 seconds
play_note("D", 0.5, 4)  # Play D4 for 0.5 seconds
play_note("E", 0.5, 4)  # Play E4 for 0.5 seconds
play_note("F", 0.5, 4)
play_note("G", 0.5, 4)
play_note("A", 0.5, 4)
play_note("B", 0.5, 4)
play_note("C", 1, 5)  # Play C5 for 1 second

# Create a simple melody (C major scale)
notes = ["C", "D", "E", "F", "G", "A", "B", "C"]
for note in notes:
    play_note(note, 0.3, 4)