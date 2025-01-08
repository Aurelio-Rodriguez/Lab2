def navigate_file():
  while True:
    filename = input("Enter filename (or 'exit' to quit): ")
    if filename.lower() == "exit":
      print("Exiting program.")
      break

    try:
      with open(filename, "r") as file:
        lines = file.readlines()
        print(f"The file has {len(lines)} lines.")

        while True:
          try:
            line_number = int(input("Enter a line number (0 to exit): "))
            if line_number == 0:
              print("Returning to file selection.")
              break
            elif 1 <= line_number <= len(lines):
              print(lines[line_number - 1].strip())
            else:
              print("Invalid line number.")
          except ValueError:
            print("Please enter a valid number.")
    except FileNotFoundError:
      print("File not found. Please try again.")

if __name__ == "__main__":
  navigate_file()
