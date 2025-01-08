def load_words(filename):
  try:
    with open(filename, "r") as file:
      words = file.read().splitlines()
      return tuple(words)
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return ()

def main():
  nouns = load_words("nouns.txt")
  verbs = load_words("verbs.txt")
  articles = load_words("articles.txt")
  prepositions = load_words("prepositions.txt")

  if nouns and verbs and articles and prepositions:
    print("Words loaded successfully.")
    print(f"Nouns: {nouns}")
    print(f"Verbs: {verbs}")
    print(f"Articles: {articles}")
    print(f"Prepositions: {prepositions}")

  else:
    print("Failed to load some files.")

if __name__ == "__main__":
  main()
