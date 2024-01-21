def print_grid(row, col):
    for i in range(1, 6):
        for j in range(1, 6):
            if i == row and j == col:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

def main():
    try:
        row = int(input("Enter the row number (1-5): "))
        col = int(input("Enter the column number (1-5): "))

        if 1 <= row <= 5 and 1 <= col <= 5:
            print_grid(row, col)
        else:
            print("Please enter valid row and column numbers (1-5).")
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
