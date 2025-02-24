import sounddevice as sd
import numpy as np

def frequency(note_name, octave=4, a4_frequency=440):
    """Calculates the frequency of a musical note."""
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note_name.upper())

    a4_index = notes.index("A")
    semitones_from_a4 = note_index - a4_index + (octave - 4) * 12

    return a4_frequency * (2 ** (semitones_from_a4 / 12))

def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    """Generates a sine wave at a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    return wave * amplitude #add amplitude control

def play_note(note_name, duration, octave=4, sample_rate=44100, amplitude=0.5):
    """Plays a musical note for a given duration."""
    freq = frequency(note_name, octave)
    wave = generate_sine_wave(freq, duration, sample_rate, amplitude)
    sd.play(wave, sample_rate)
    sd.wait()

# Mario Theme Melody (Simplified) - adjusted based on video
mario_melody = [
    ("E", 4, 0.125), ("E", 4, 0.125), ("E", 4, 0.25), ("C", 4, 0.125), ("E", 4, 0.25),
    ("G", 4, 0.375), ("G", 3, 0.333),
    ("C", 4, 0.125), ("G", 3, 0.25), ("E", 3, 0.25), ("A", 3, 0.25),
    ("B", 3, 0.25), ("A#", 3, 0.166), ("A", 3, 0.25), ("G", 3, 0.5), ("E", 4, 0.125),
    ("G", 4, 0.125), ("A", 4, 0.166), ("F", 4, 0.125), ("G", 4, 0.125), ("E", 4, 0.25),
    ("C", 4, 0.125), ("D", 4, 0.125), ("B", 3, 0.25), ("C", 4, 0.375), ("G", 3, 0.333),
]

for note, octave, duration in mario_melody:
    play_note(note, duration, octave)