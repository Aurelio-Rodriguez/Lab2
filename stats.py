def mean(numbers):
    """Compute the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def main():
    """Test the statistical functions with a sample list."""
    sample_numbers = [10, 20, 20, 30, 40, 50, 50, 50, 60]
    print("Sample numbers:", sample_numbers)
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))

if __name__ == "__main__":
    main()
