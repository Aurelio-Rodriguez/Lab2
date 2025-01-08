# generator_modified.py

import random
import os

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    try:
        # Ensure the file path is relative to the script's directory
        script_dir = os.path.dirname(__file__)  # Directory of the script
        file_path = os.path.join(script_dir, filename)
        
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return tuple(words)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ()

def sentence():
    """Builds and returns a sentence."""
    return f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(prepositions)} {random.choice(articles)} {random.choice(nouns)}."

# Load vocabulary from text files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def main():
    """Generate random sentences."""
    if not (articles and nouns and verbs and prepositions):
        print("Error: Missing or empty vocabulary files.")
        return
    
    number_of_sentences = int(input("Enter the number of sentences to generate: "))
    for _ in range(number_of_sentences):
        print(sentence())

if __name__ == "__main__":
    main()
