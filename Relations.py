import math
import matplotlib.pyplot as plt
import numpy as np

def frequency_ratio(interval_name):
    """Calculates the frequency ratio for a given interval."""
    intervals = {
        "octave": 2/1,
        "perfect fifth": 3/2,
        "perfect fourth": 4/3,
        "major third": 5/4,
        "minor third": 6/5,
    }
    return intervals.get(interval_name.lower(), "Interval not found")

def equal_temperament_ratio(semitones):
    """Calculates the frequency ratio for a given number of semitones in equal temperament."""
    return 2 ** (semitones / 12)

def calculate_cents(ratio):
    """Calculates the number of cents for a given frequency ratio."""
    return 1200 * math.log2(ratio)

# Example usage:
print("Frequency ratio of an octave:", frequency_ratio("octave"))
print("Frequency ratio of a perfect fifth:", frequency_ratio("perfect fifth"))
print("Frequency ratio of a perfect fourth:", frequency_ratio("perfect fourth"))
print("Frequency ratio of a major third:", frequency_ratio("major third"))
print("Frequency ratio of a minor third:", frequency_ratio("minor third"))

print("\nEqual temperament ratios:")
print("Frequency ratio of 1 semitone:", equal_temperament_ratio(1))
print("Frequency ratio of 12 semitones (octave):", equal_temperament_ratio(12))

print("\nCents calculations:")
perfect_fifth_ratio = frequency_ratio("perfect fifth")
print(f"Cents for a perfect fifth (3/2): {calculate_cents(perfect_fifth_ratio)}")

equal_temp_fifth = equal_temperament_ratio(7) # seven semitones is a fifth.
print(f"Cents for an equal tempered fifth: {calculate_cents(equal_temp_fifth)}")

#Example to show the difference between just intonation and equal temperament.
just_major_third = frequency_ratio("major third")
equal_temp_major_third = equal_temperament_ratio(4) #4 semitones is a major third.
print(f"Cents difference between just and equal major third: {calculate_cents(just_major_third) - calculate_cents(equal_temp_major_third)}")

# Plotting frequency ratios of common intervals
intervals = ["Octave", "Perfect Fifth", "Perfect Fourth", "Major Third", "Minor Third"]
ratios = [frequency_ratio(interval.lower()) for interval in intervals]

plt.figure(figsize=(10, 5))
plt.bar(intervals, ratios)
plt.ylabel("Frequency Ratio")
plt.title("Frequency Ratios of Common Intervals")
plt.show()

# Plotting equal temperament
semitones = np.arange(0, 13)  # 0 to 12 semitones (1 octave)
equal_temp_ratios = [equal_temperament_ratio(s) for s in semitones]

plt.figure(figsize=(10, 5))
plt.plot(semitones, equal_temp_ratios, marker='o')
plt.xticks(semitones)
plt.xlabel("Semitones")
plt.ylabel("Frequency Ratio")
plt.title("Equal Temperament: Frequency Ratios per Semitone")
plt.grid(True)
plt.show()
