import math

# Frequencies of musical notes up to 8000 Hz
note_frequencies = {
    "C0": 16.35, "C#0": 17.32, "D0": 18.35, "D#0": 19.45, "E0": 20.60, "F0": 21.83, "F#0": 23.12, "G0": 24.50,
    "G#0": 25.96, "A0": 27.50, "A#0": 29.14, "B0": 30.87, "C1": 32.70, "C#1": 34.65, "D1": 36.71, "D#1": 38.89,
    "E1": 41.20, "F1": 43.65, "F#1": 46.25, "G1": 49.00, "G#1": 51.91, "A1": 55.00, "A#1": 58.27, "B1": 61.74,
    "C2": 65.41, "C#2": 69.30, "D2": 73.42, "D#2": 77.78, "E2": 82.41, "F2": 87.31, "F#2": 92.50, "G2": 98.00,
    "G#2": 103.83, "A2": 110.00, "A#2": 116.54, "B2": 123.47, "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56,
    "E3": 164.81, "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65, "A3": 220.00, "A#3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00,
    "G#4": 415.30, "A4": 440.00, "A#4": 466.16, "B4": 493.88, "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25,
    "E5": 659.26, "F5": 698.46, "F#5": 739.99, "G5": 783.99, "G#5": 830.61, "A5": 880.00, "A#5": 932.33, "B5": 987.77,
    "C6": 1046.50, "C#6": 1108.73, "D6": 1174.66, "D#6": 1244.51, "E6": 1318.51, "F6": 1396.91, "F#6": 1479.98, "G6": 1567.98,
    "G#6": 1661.22, "A6": 1760.00, "A#6": 1864.66, "B6": 1975.53, "C7": 2093.00, "C#7": 2217.46, "D7": 2349.32, "D#7": 2490.91,
    "E7": 2637.02, "F7": 2793.83, "F#7": 2959.96, "G7": 3135.96, "G#7": 3322.44, "A7": 3520.00, "A#7": 3729.31, "B7": 3951.07,
    "C8": 4186.01, "C#8": 4434.92, "D8": 4698.64, "D#8": 4981.82, "E8": 5274.04, "F8": 5587.66, "F#8": 5919.92, "G8": 6271.92,
    "G#8": 6644.88, "A8": 7040.00, "A#8": 7458.62, "B8": 7902.14, "C9": 8372.02
}

def calculate_note(frequency):
    """Calculates the closest musical note to a given frequency and returns the signed Cents."""
    best_note = None
    smallest_difference = float("inf")

    for note, freq in note_frequencies.items():
        difference = abs(frequency - freq)
        if difference < smallest_difference:
            best_note = note
            smallest_difference = difference

    cents = 1200 * math.log2(frequency / note_frequencies[best_note])
    sign = "+" if cents > 0 else "" if cents < 0 else "0"

    return best_note, cents, sign

def calculate_multiples(n, kind="odd"):
    """Calculates odd or even multiples of a number n up to 20000."""
    if n <= 0:
        raise ValueError("The number must be positive.")

    multiples = []
    multiple = 1 if kind == "odd" else 2

    while True:
        result = n * multiple
        if result > 20000:
            break
        multiples.append(result)
        multiple += 2

    return multiples

def display_multiple_series(n):
    """Displays all multiples of a frequency and their musical notes."""
    print(f"\nMultiple series for frequency {n} Hz:")

    odd_multiples = calculate_multiples(n, "odd")
    even_multiples = calculate_multiples(n, "even")

    for m in odd_multiples + even_multiples:
        note, cents, sign = calculate_note(m)
        print(f"{m:.2f} Hz - Note: {note} - Cents: {sign}{cents:.2f}")

def count_common_multiples(n1, n2):
    """Counts how many odd and even multiples are common between n1 and n2."""
    odd_multiples_n1 = set(calculate_multiples(n1, "odd"))
    odd_multiples_n2 = set(calculate_multiples(n2, "odd"))

    even_multiples_n1 = set(calculate_multiples(n1, "even"))
    even_multiples_n2 = set(calculate_multiples(n2, "even"))

    common_odd = odd_multiples_n1.intersection(odd_multiples_n2)
    common_even = even_multiples_n1.intersection(even_multiples_n2)

    total_common = len(common_odd) + len(common_even)
    return len(common_odd), len(common_even), total_common

def find_all_common_numbers(n):
    """Finds numbers between 20 and 8372.02 that share more than 5 odd/even multiples with n."""
    common_numbers = []

    num = 20.0
    while num <= 8372.02:
        if num != n:
            odd_count, even_count, total_common = count_common_multiples(n, num)
            if total_common > 5:
                common_numbers.append((num, odd_count, even_count, total_common))
        num = round(num + 0.01, 2)

    common_numbers.sort(key=lambda x: x[3], reverse=True)
    return common_numbers

# Example usage
number = float(input("Enter a sound frequency between 20 and 20000: "))
try:
    display_multiple_series(number)

    common_numbers = find_all_common_numbers(number)

    print(f"\nListing the first 200 numbers that share more than 5 multiples with {number} Hz:")
    for num, odd_count, even_count, total_common in common_numbers[:200]:
        note, cents, sign = calculate_note(num)
        print(f"{num:.2f} Hz - Note: {note} - Cents: {sign}{cents:.2f} - Common multiples: {total_common} (Odd: {odd_count}, Even: {even_count})")

except ValueError as e:
    print(e)
