# stats.py

def mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)  # Sort a copy to avoid modifying the original list
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1, mid2 = sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    # Return the mode or a list of modes if multiple values share the maximum frequency
    return modes[0] if len(modes) == 1 else modes

def main():
    """Test the mean, median, and mode functions."""
    test_numbers = [7, 3, 1, 4, 3, 9, 3, 8, 7, 7]
    print("Test List:", test_numbers)
    print(f"Mean: {mean(test_numbers):.2f}")
    print(f"Median: {median(test_numbers):.2f}")
    mode_result = mode(test_numbers)
    print(f"Mode: {mode_result if isinstance(mode_result, list) else [mode_result]}")

if __name__ == "__main__":
    main()
