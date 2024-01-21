def main():
    user_input = input("Enter a string: ")

    characters = list(user_input)

    nested_lists = [characters[i:i+3] for i in range(0, len(characters), 3)]

    print("List of Characters:", characters)
    print("List of Lists (3 elements each):", nested_lists)

if __name__ == "__main__":
    main()
