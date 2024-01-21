def main():
    try:
        list1 = [int(input(f"Enter integer for list 1 ({i+1}/5): ")) for i in range(5)]

        list2 = [int(input(f"Enter integer for list 2 ({i+1}/5): ")) for i in range(5)]

        common_values = list(set(list1) & set(list2))

        print("List 1:", list1)
        print("List 2:", list2)
        print("Common Values:", common_values)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
