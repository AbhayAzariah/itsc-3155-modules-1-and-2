def main():
    numbers = []
    even_numbers = []

    while True:
        user_input = input("Enter a number (type 'QUIT' to stop): ")

        if user_input.upper() == "QUIT":
            break

        try:
            num = int(user_input)
            numbers.append(num)
            if num % 2 == 0:
                even_numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'QUIT'.")

    print("All Numbers:", numbers)
    print("Even Numbers:", even_numbers)

if __name__ == "__main__":
    main()
