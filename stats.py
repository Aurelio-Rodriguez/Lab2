# stats.py
def mean(numbers):
    """Returns the mean (average) of the numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Returns the median of the numbers."""
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    """Returns the mode of the numbers."""
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def main():
    """Tests the statistical functions."""
    sample_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Numbers:", sample_numbers)
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))

if __name__ == "__main__":
    main()
