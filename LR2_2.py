# LR2_2.py

def main():
    """Navigate the lines of a text file."""
    try:
        # Prompt for the file name and read lines
        file_name = input("Enter the filename: ")
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file]  # Strip newline characters
        
        total_lines = len(lines)
        print(f"The file contains {total_lines} line(s).")

        while True:
            # Prompt the user for a line number
            line_input = input("Enter a line number (0 to quit): ")
            if not line_input.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            line_number = int(line_input)

            if line_number == 0:
                print("Goodbye!")
                break
            elif 1 <= line_number <= total_lines:
                print(f"Line {line_number}: {lines[line_number - 1]}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {total_lines}.")
    except FileNotFoundError:
        print("Error: File not found. Please ensure the filename is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
