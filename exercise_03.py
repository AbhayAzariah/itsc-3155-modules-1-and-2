def print_cubes_up_to_n(n):
    for i in range(n + 1):
        cube = i ** 3
        print(f"The cube of {i} is: {cube}")

def main():
    try:
       
        n = int(input("Enter an integer greater than 1: "))
        
        
        if n > 1:
           
            print_cubes_up_to_n(n)
        else:
            print("Please enter an integer greater than 1.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
