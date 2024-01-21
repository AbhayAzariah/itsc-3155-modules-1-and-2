def main():
    words = []

    for i in range(5):
        word = input(f"Enter word {i + 1}/5: ")
        words.append(word)

    result_string = " ".join(words)

    print("List of Words:", words)
    print("Resultant String:", result_string)

if __name__ == "__main__":
    main()
