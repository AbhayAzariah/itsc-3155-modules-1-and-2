def shift_lowercase_to_front(input_string):
 
    lower_case = ''.join(char for char in input_string if char.islower())
    upper_case = ''.join(char for char in input_string if char.isupper())


    input_string = input_string.replace(" ", "")

   
    result_string = lower_case + upper_case

    print("Result:", result_string)

user_input = input("Enter a string: ")


shift_lowercase_to_front(user_input)
