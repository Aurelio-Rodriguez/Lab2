# LR2_2.py

def main():
    """Navigate through the lines of text in a file."""
    try:
        # Prompt user for a filename
        file_name = input("Enter the filename: ")
        with open(file_name, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
        
        print(f"The file has {len(lines)} line(s).")
        while True:
            # Prompt for a line number
            try:
                line_number = int(input("Enter a line number (0 to quit): "))
                if line_number == 0:
                    print("Exiting the program.")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")
            except ValueError:
                print("Please enter a valid number.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
