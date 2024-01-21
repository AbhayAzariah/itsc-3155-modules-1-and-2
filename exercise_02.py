def check_suffix(str1, str2):
   
    return str1.endswith(str2) or str2.endswith(str1)

def main():
    
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    result = check_suffix(str1, str2)

    print(result)

if __name__ == "__main__":
    main()
