def main():
    numbers = []
    unique_numbers = []

    for i in range(10):
        while True:
            user_input = input(f"Enter integer {i + 1}/10: ")

            try:
                num = int(user_input)
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    for num in numbers:
        if numbers.count(num) == 1:
            unique_numbers.append(num)

    print("All Numbers:", numbers)
    print("Numbers that occured once:", unique_numbers)

if __name__ == "__main__":
    main()
