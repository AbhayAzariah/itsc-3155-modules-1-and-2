def calculate_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def main():
   
    try:
        grade = int(input("Enter your grade (0-100): "))
        
      
        if 0 <= grade <= 100:
            letter_grade = calculate_letter_grade(grade)
            print(f"Your letter grade is: {letter_grade}")
        else:
            print("Please enter a valid grade between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numerical grade.")

if __name__ == "__main__":
    main()
