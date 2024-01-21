def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    try:
        
        n = int(input("Enter the number of values: "))
        
        
        numbers = []
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)

        
        print("List of numbers:", numbers)

        
        mean = calculate_mean(numbers)
        print("Mean:", mean)
    except ValueError:
        print("Invalid input. Please enter a valid number or float.")

if __name__ == "__main__":
    main()
